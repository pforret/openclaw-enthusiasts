#!/usr/bin/env bash
# Download an image from a URL to a local path
# Usage: download_image.sh <url> <output_path>
set -euo pipefail

URL="$1"
OUTPUT="$2"

if [[ -z "$URL" || -z "$OUTPUT" ]]; then
  echo "Usage: download_image.sh <url> <output_path>" >&2
  exit 1
fi

# Create output directory if needed
mkdir -p "$(dirname "$OUTPUT")"

# Download with curl, follow redirects, fail on HTTP errors
curl -fsSL -o "$OUTPUT" "$URL"

if [[ -f "$OUTPUT" ]]; then
  echo "Downloaded: $OUTPUT ($(wc -c < "$OUTPUT") bytes)"
else
  echo "Error: download failed" >&2
  exit 1
fi
