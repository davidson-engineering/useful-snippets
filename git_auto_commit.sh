#!/bin/bash

# Set the repository path to the first argument, or use the current directory if no argument is provided
REPO_PATH="${1:-$(pwd)}"

# Log file location inside the repository path
LOG_FILE="$REPO_PATH/.git_auto_commit.log"

# Navigate to the repository
if [ -d "$REPO_PATH" ]; then
  cd "$REPO_PATH" || { echo "Failed to navigate to repository path: $REPO_PATH" | tee -a "$LOG_FILE"; exit 1; }
else
  echo "Invalid repository path: $REPO_PATH" | tee -a "$LOG_FILE"
  exit 1
fi

# Ensure the logfile is ignored by Git
GIT_IGNORE_PATH = "$REPO_PATH/.gitignore"
if [ -f "$GIT_IGNORE_PATH" ]; then
  if ! grep -qxF "$(basename "$LOG_FILE")" "$GIT_IGNORE_PATH"; then
    echo "$(basename "$LOG_FILE")" >> "$GIT_IGNORE_PATH"
    echo "Added $(basename "$LOG_FILE") to .gitignore"
  fi
else
  echo ".gitignore does not exist. Creating and adding $(basename "$LOG_FILE")..."
  echo "$(basename "$LOG_FILE")" > "$GIT_IGNORE_PATH"
fi

# Start logging
{
  echo "---------------------------------------------"
  echo "Script started on $(date)"
  echo "Working directory: $REPO_PATH"

  # Pull the latest changes from the remote repository
  echo "Pulling the latest changes from the remote repository..."
  git pull

  # Check if there are any changes in the working directory
  echo "Checking for changes..."
  if git diff --quiet && git diff --cached --quiet; then
    echo "No changes detected. Exiting."
    exit 0
  else
    echo "Changes detected. Preparing to commit and push..."
  fi

  # Stage all changes
  git add .

  # Commit the changes
  COMMIT_MESSAGE="Automated commit on $(date)"
  git commit -m "$COMMIT_MESSAGE"

  # Push the changes to the remote repository
  echo "Pushing changes to the remote repository..."
  git push

  echo "Changes successfully pushed!"
  echo "Script ended on $(date)"
} >> "$LOG_FILE" 2>&1

