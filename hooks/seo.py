"""MkDocs hook: auto-generates llms-full.txt from blog posts."""

import os
import re
from datetime import datetime


def on_pre_build(config, **kwargs):
    posts_dir = os.path.join(config["docs_dir"], "blog", "posts")
    if not os.path.isdir(posts_dir):
        return

    posts = []
    for filename in sorted(os.listdir(posts_dir), reverse=True):
        if not filename.endswith(".md"):
            continue

        with open(os.path.join(posts_dir, filename)) as f:
            content = f.read()

        fm_match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
        if not fm_match:
            continue
        frontmatter, body = fm_match.group(1), fm_match.group(2).strip()

        date_match = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", frontmatter, re.MULTILINE)
        if not date_match:
            continue
        date_str = date_match.group(1)

        slug_match = re.search(r"^slug:\s*(.+)", frontmatter, re.MULTILINE)
        desc_match = re.search(r'^description:\s*["\']?(.+?)["\']?\s*$', frontmatter, re.MULTILINE)

        title_match = re.search(r"^#\s+(.+)", body, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filename

        if slug_match:
            slug = slug_match.group(1).strip()
        else:
            slug = re.sub(r"[^\w\s-]", "", title.lower())
            slug = re.sub(r"[\s_]+", "-", slug).strip("-")

        url = f"https://openclaw.mkdox.com/blog/{date_str[:4]}/{date_str[5:7]}/{slug}/"
        description = desc_match.group(1).strip() if desc_match else ""

        posts.append((date_str, title, url, description))

    posts.sort(key=lambda p: p[0], reverse=True)

    lines = [
        "# OpenClaw Enthusiasts — Full Post Index",
        "",
        f"> {len(posts)} blog posts about practical OpenClaw automation use cases.",
        "",
    ]
    for date_str, title, url, description in posts:
        lines.append(f"## {title}")
        lines.append(f"- URL: {url}")
        lines.append(f"- Date: {date_str}")
        if description:
            lines.append(f"- Description: {description}")
        lines.append("")

    output_path = os.path.join(config["docs_dir"], "llms-full.txt")
    with open(output_path, "w") as f:
        f.write("\n".join(lines))
