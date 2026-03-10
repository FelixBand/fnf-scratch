#!/bin/bash

# Define file and folder names
output_file="Friday Night Funkin'.sb3"
input_folder="Friday Night Funkin'"

# Check if the SB3 file already exists
if [ -f "$output_file" ]; then
  # Use macOS-compatible stat command
  last_modified=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$output_file")
  echo "This version is from: $last_modified"
  
  # Prompt the user
  read -p "Replace older already existing version? Y/n: " response

  # Handle response
  if [[ "$response" =~ ^[Yy]$ || -z "$response" ]]; then
    rm "$output_file"
    zip -r "$output_file" "$input_folder"/*
    echo "File replaced successfully."
  else
    echo "Operation canceled."
  fi
else
  # If file doesn't exist, create it
  zip -r "$output_file" "$input_folder"/*
  echo "File created successfully."
fi