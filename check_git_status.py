from git_helper import run_git_command

def check_git_status():
    output = "Remote repositories:\n"
    output += run_git_command("remote -v")
    output += "\nGit status:\n"
    output += run_git_command("status")
    output += "\nRecent commits:\n"
    output += run_git_command("log --oneline -n 5")
    
    with open("git_status_output.txt", "w") as f:
        f.write(output)

if __name__ == "__main__":
    check_git_status()
    print("Git status check completed. Results written to git_status_output.txt")