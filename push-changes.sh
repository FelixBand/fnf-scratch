#!/bin/bash

# Define variables
sb3_file="Friday Night Funkin'.sb3"
extract_folder="Friday Night Funkin'"

# Check if SB3 file exists
if [ ! -f "$sb3_file" ]; then
  echo "Error: $sb3_file not found."
  exit 1
fi

# Remove old extracted folder if it exists
if [ -d "$extract_folder" ]; then
  rm -rf "$extract_folder"
fi

# Create extraction folder
mkdir "$extract_folder"

# Extract contents without nesting
unzip -j "$sb3_file" -d "$extract_folder" || { echo "Extraction failed."; exit 1; }

# Stage changes
git add .

# Commit changes with a timestamp
commit_msg="Updated project - $(date "+%Y-%m-%d %H:%M:%S")"
git commit -m "$commit_msg"

# Push changes
git push || { echo "Push failed."; exit 1; }

echo "Changes successfully pushed!"