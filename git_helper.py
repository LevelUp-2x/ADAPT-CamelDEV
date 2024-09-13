import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(f"git {command}", shell=True, check=True, capture_output=True, text=True)
        print(f"Command output for 'git {command}':")
        print(result.stdout)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing 'git {command}':")
        print(e.stderr)
        return f"Error: {e.stderr}"