#!/bin/bash

# Author: ChatGPT

# Ensure ImageMagick is installed
if ! command -v convert &> /dev/null; then
  echo "ImageMagick is not installed. Please install it first."
  exit 1
fi

# Check if an input SVG is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <input.svg>"
  exit 1
fi

INPUT_SVG="$1"

# Check if the input file exists
if [ ! -f "$INPUT_SVG" ]; then
  echo "File $INPUT_SVG not found!"
  exit 1
fi

# Output directory
OUTPUT_DIR="icons"
mkdir -p "$OUTPUT_DIR"

# Define sizes for PWA icons
SIZES=(48 72 96 128 144 152 192 384 512)

# Generate icons in various sizes
echo "Generating PWA icons..."
for SIZE in "${SIZES[@]}"; do
  OUTPUT_FILE="$OUTPUT_DIR/icon-${SIZE}x${SIZE}.png"
  convert -background none -resize "${SIZE}x${SIZE}" "$INPUT_SVG" "$OUTPUT_FILE"
  echo "Created $OUTPUT_FILE"
done

# Generate favicon (16x16, 32x32, and 48x48 ICO file)
echo "Generating favicon..."
convert -background none -resize 16x16 "$INPUT_SVG" "$OUTPUT_DIR/favicon-16x16.png"
convert -background none -resize 32x32 "$INPUT_SVG" "$OUTPUT_DIR/favicon-32x32.png"
convert -background none -resize 48x48 "$INPUT_SVG" "$OUTPUT_DIR/favicon-48x48.png"
convert "$OUTPUT_DIR/favicon-16x16.png" "$OUTPUT_DIR/favicon-32x32.png" "$OUTPUT_DIR/favicon-48x48.png" "$OUTPUT_DIR/favicon.ico"

echo "All icons and favicon have been generated in the $OUTPUT_DIR directory!"

cp "$OUTPUT_DIR/favicon.ico" .
