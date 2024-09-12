import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(f"git {command}", shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"