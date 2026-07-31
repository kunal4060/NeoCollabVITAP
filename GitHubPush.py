#!/usr/bin/env python3
"""
gitpush.py - Stage all changes, commit with a message you enter, and push to GitHub

Usage:
    python gitpush.py
"""

import subprocess
import sys


def run(cmd, check=True):
    """Run a shell command and return (returncode, stdout, stderr)."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error running: {' '.join(cmd)}")
        print(result.stderr.strip())
        sys.exit(1)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def main():
    # Make sure we're inside a git repo
    code, _, _ = run(["git", "rev-parse", "--is-inside-work-tree"], check=False)
    if code != 0:
        print("Error: This folder is not a git repository.")
        sys.exit(1)

    # Show current changes
    _, status_output, _ = run(["git", "status", "--short"])
    if not status_output:
        print("Nothing to commit. Working tree is clean.")
        sys.exit(0)

    print("Changes detected:")
    print(status_output)

    # Ask for commit message
    commit_msg = input("Enter commit message: ").strip()
    if not commit_msg:
        print("Commit message cannot be empty. Aborting.")
        sys.exit(1)

    # Stage all changes
    run(["git", "add", "-A"])

    # Commit
    run(["git", "commit", "-m", commit_msg])

    # Get current branch
    _, branch, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])

    
    print(f"Pushing to origin/{branch} ...")
    run(["git", "push", "origin", branch])

    print(f"Done! Changes pushed to origin/{branch}")


if __name__ == "__main__":
    main()