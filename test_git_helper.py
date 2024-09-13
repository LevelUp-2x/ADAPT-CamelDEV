from git_helper import run_git_command

# Test the git status command
status_output = run_git_command("status")
print("Git Status Output:")
print(status_output)

# Test the git log command (last 5 commits)
log_output = run_git_command("log -n 5 --oneline")
print("\nGit Log Output (last 5 commits):")
print(log_output)