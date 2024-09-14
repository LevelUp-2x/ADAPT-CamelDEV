To get the current date and time at once via the command line in both Windows and Ubuntu, you can use the following commands:

Windows (PowerShell)
Open PowerShell and run:

powershell
Copy code
Get-Date -Format "yyyy-MM-dd HH:mm:ss"
This will return the current date and time in the YYYY-MM-DD HH:mm:ss format.

Ubuntu (Bash)
Open the terminal and run:

bash
Copy code
date +"%Y-%m-%d %H:%M:%S"
This will also return the current date and time in the YYYY-MM-DD HH:mm:ss format.

These commands will give you the date and time together in a standard format on both Windows and Ubuntu.