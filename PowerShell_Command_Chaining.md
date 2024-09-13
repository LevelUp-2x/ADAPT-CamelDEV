# PowerShell Command Chaining

In PowerShell, you can string commands together using several different operators and methods. Here are some common ways to do it:

## 1. Using Semicolon (;)
The semicolon allows you to run multiple commands sequentially on the same line.

```powershell
command1; command2; command3
```

## 2. Using the Pipeline (|)
The pipeline operator passes the output of one command as input to the next command.

```powershell
command1 | command2 | command3
```

## 3. Using the Ampersand (&)
The ampersand is used to call a command, script, or function. It is particularly useful when you need to run a command stored in a variable.

```powershell
& command1
```

## 4. Using the Backtick (`)
The backtick is used for line continuation, allowing you to split a long command across multiple lines.

```powershell
command1 `
command2 `
command3
```

## 5. Using the Start-Process Cmdlet
The Start-Process cmdlet can be used to run commands in a new process.

```powershell
Start-Process -FilePath "command1"
Start-Process -FilePath "command2"
Start-Process -FilePath "command3"
```

## 6. Using the Invoke-Command Cmdlet
The Invoke-Command cmdlet can be used to run commands on local or remote computers.

```powershell
Invoke-Command -ScriptBlock { command1; command2; command3 }
```

## Examples

Here's an example of stringing commands together using the semicolon:

```powershell
Get-Process; Get-Service; Get-EventLog -LogName Application
```

And here's an example using the pipeline:

```powershell
Get-Process | Where-Object { $_.CPU -gt 10 } | Sort-Object -Property CPU -Descending
```

Choose the method that best fits your needs based on the specific requirements of your script or command sequence.