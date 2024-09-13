import subprocess
import time
import os
import logging

# Set up logging
logging.basicConfig(filename='git_auto_push.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def check_for_changes():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, check=True)
        return bool(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        logging.error(f"Error checking git status: {e}")
        return False

def git_push():
    try:
        if not check_for_changes():
            logging.info("No changes to commit.")
            return

        # Add all changes
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit changes with timestamp
        commit_message = f"Auto-commit: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push changes
        subprocess.run(["git", "push"], check=True)
        
        logging.info(f"Changes pushed successfully at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    except subprocess.CalledProcessError as e:
        if "Authentication failed" in str(e):
            logging.error("Git authentication failed. Please check your credentials.")
        else:
            logging.error(f"Error during git operations: {e}")

def open_progress_file():
    progress_file_path = r"C:\Users\ChaseRemmen\ADAPT\ADAPT-CamelDEV\Project-Progress\ADAPT-CamelDEV.md"
    try:
        os.startfile(progress_file_path)
        logging.info(f"Opened progress file: {progress_file_path}")
    except Exception as e:
        logging.error(f"Error opening progress file: {e}")

if __name__ == "__main__":
    logging.info("Running auto-push script")
    git_push()
    open_progress_file()