#!/bin/bash

# Configuration
TARGET_DIR="$HOME/Projects"
REPO_URL=$1

# Check if URL was passed as an argument
if [ -z "$REPO_URL" ]; then
    echo "Usage: $0 <github-repo-url>"
    exit 1
fi

# Create target directory if it doesn't exist
mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR" || exit

# Extract folder name
FOLDER_NAME=$(basename "$REPO_URL" .git)

# Process repository
if git clone "$REPO_URL"; then
    code "$TARGET_DIR/$FOLDER_NAME"
else
    echo "Failed to clone repository."
    exit 1
fi
