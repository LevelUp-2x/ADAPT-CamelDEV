import subprocess
import time
import os

def git_push():
    try:
        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit changes with timestamp
        commit_message = f"Auto-commit: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push changes
        subprocess.run(["git", "push"], check=True)
        
        print(f"Changes pushed successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")

def open_progress_file():
    progress_file_path = r"C:\Users\ChaseRemmen\ADAPT\ADAPT-CamelDEV\Project-Progress\ADAPT-CamelDEV.md"
    try:
        os.startfile(progress_file_path)
        print(f"Opened progress file: {progress_file_path}")
    except Exception as e:
        print(f"Error opening progress file: {e}")

def main():
    while True:
        git_push()
        open_progress_file()
        time.sleep(600)  # Wait for 10 minutes (600 seconds)

if __name__ == "__main__":
    main()