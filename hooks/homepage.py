"""MkDocs hook: generates a responsive 3-column post grid on the homepage."""

import os
import re
from datetime import datetime


def on_config(config, **kwargs):
    version_file = os.path.join(os.path.dirname(config["config_file_path"]), "VERSION.md")
    if os.path.exists(version_file):
        with open(version_file) as f:
            version = f.read().strip()
        if version:
            config["copyright"] = config.get("copyright", "") + f" &bull; v{version}"
    return config


def on_page_markdown(markdown, page, config, files, **kwargs):
    if page.file.src_path != "index.md":
        return markdown

    posts_dir = os.path.join(config["docs_dir"], "blog", "posts")
    posts = []

    for filename in sorted(os.listdir(posts_dir), reverse=True):
        if not filename.endswith(".md"):
            continue

        with open(os.path.join(posts_dir, filename)) as f:
            content = f.read()

        # Parse frontmatter
        fm_match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
        if not fm_match:
            continue
        frontmatter, body = fm_match.group(1), fm_match.group(2).strip()

        # Date
        date_match = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", frontmatter, re.MULTILINE)
        if not date_match:
            continue
        date_str = date_match.group(1)
        date = datetime.strptime(date_str, "%Y-%m-%d")

        # Image
        image_match = re.search(r"^image:\s*(.+)", frontmatter, re.MULTILINE)
        image = image_match.group(1).strip() if image_match else ""

        # Title (first # heading)
        title_match = re.search(r"^#\s+(.+)", body, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filename

        # Excerpt: text between title and <!-- more -->
        body_after_title = re.sub(r"^#\s+.+\n*", "", body, count=1).strip()
        more_pos = body_after_title.find("<!-- more -->")
        if more_pos > 0:
            excerpt = body_after_title[:more_pos].strip()
        else:
            excerpt = body_after_title.split("\n\n")[0].strip()

        # Strip markdown formatting from excerpt
        excerpt = re.sub(r"!\[.*?\]\(.*?\)", "", excerpt)
        excerpt = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", excerpt)
        excerpt = re.sub(r"\*\*(.+?)\*\*", r"\1", excerpt)
        excerpt = re.sub(r"\*(.+?)\*", r"\1", excerpt)
        excerpt = excerpt.strip()

        # Limit to 100 words
        words = excerpt.split()
        if len(words) > 100:
            excerpt = " ".join(words[:100]) + " ..."

        # Build URL: blog/YYYY/MM/slug/ (use frontmatter slug if set, else derive from title)
        slug_match = re.search(r"^slug:\s*(.+)", frontmatter, re.MULTILINE)
        if slug_match:
            slug = slug_match.group(1).strip()
        else:
            slug = re.sub(r"[^\w\s-]", "", title.lower())
            slug = re.sub(r"[\s_]+", "-", slug).strip("-")
        url = f"blog/{date_str[:4]}/{date_str[5:7]}/{slug}/"

        posts.append(
            {
                "title": title,
                "date": date,
                "date_str": date.strftime("%b %d, %Y"),
                "image": image,
                "excerpt": excerpt,
                "url": url,
            }
        )

    posts.sort(key=lambda p: p["date"], reverse=True)
    posts = posts[:12]

    cards = []
    for post in posts:
        img = ""
        if post["image"]:
            img = f'<img src="{post["image"]}" alt="{post["title"]}" loading="lazy">'

        cards.append(
            f'<a class="post-card" href="{post["url"]}">'
            f'<div class="post-card__image">{img}</div>'
            f'<div class="post-card__content">'
            f'<time class="post-card__date">{post["date_str"]}</time>'
            f'<h2 class="post-card__title">{post["title"]}</h2>'
            f'<p class="post-card__excerpt">{post["excerpt"]}</p>'
            f"</div></a>"
        )

    grid = '<div class="post-grid">\n' + "\n".join(cards) + "\n</div>\n"
    return markdown + "\n\n" + grid
