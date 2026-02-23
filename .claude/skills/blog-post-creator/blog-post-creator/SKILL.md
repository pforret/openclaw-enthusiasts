---
name: blog-post-creator
description: >
  Create new blog posts for the OpenClaw MkDocs site. Use when the user asks to:
  (1) create/write a new blog post or article, (2) add a use case to the blog,
  (3) generate posts from the article source lists in articles/, or (4) create
  blog content with splash images. Handles the full workflow: pick a novel use case
  from source lists, write the post, find/download a source image, and process it
  with splashmark.
---

# Blog Post Creator

Create blog posts for the OpenClaw MkDocs site with splash images.

## Workflow

### 1. Pick a novel use case

1. Read all article source lists in `articles/list.*.md`
2. Read all existing posts in `docs/blog/posts/` (filenames suffice)
3. Identify use cases from the source lists NOT yet covered by existing posts
4. Present candidates to the user or pick one if instructed to choose

### 2. Write the blog post

1. Read `references/blog-conventions.md` for the template and style conventions
2. Determine the post date and slug
3. Fetch the source article using Jina Reader (`curl -s "https://r.jina.ai/<URL>"`) to get details for the post content
4. Write the post to `docs/blog/posts/YYYY-MM-DD-<slug>.md`

### 3. Find and download a source image

1. When fetching the source article with Jina Reader, use `--with-images` or look for image URLs in the fetched content
2. Pick an image that represents the use case (hero image, header image, or relevant illustration)
3. If no suitable image found in the article, use `splashmark unsplash "<keyword>" docs/images/<slug>.jpg` to get one
4. Download the image:
   ```bash
   bash scripts/download_image.sh "<image_url>" docs/images/<slug>.jpg
   ```

### 4. Create the splash image with splashmark

Process the downloaded image into a splash image with title overlay:

```bash
splashmark -e dark,dark,pixel,grain --preset hd -i "<Post Title>" file docs/images/<slug>.jpg docs/images/splash-<slug>.jpg
```

Parameters:
- `-e dark,dark,pixel,grain` — effect chain: darken, darken again, pixelate slightly, add grain
- `--preset hd` — HD dimensions (1920x1080)
- `-i "<Post Title>"` — the post's H1 title as overlay text
- First path: source image
- Second path: output splash image

### 5. Verify

1. Confirm `docs/images/splash-<slug>.jpg` exists
2. Confirm the post frontmatter `image:` references `images/splash-<slug>.jpg`
3. Confirm the inline image reference is `../../images/splash-<slug>.jpg`

## Resources

### scripts/
- `download_image.sh` — download an image URL to a local path

### references/
- `blog-conventions.md` — post template, frontmatter format, tag conventions, style guidelines
