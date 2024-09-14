# Start ADAPT-CamelDEV setup
Write-Host "Starting ADAPT-CamelDEV setup..."

# Set the working directory to the script's location
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $scriptPath

# Check if Python is available
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    $pythonCmd = Get-Command python3 -ErrorAction SilentlyContinue
}

if (-not $pythonCmd) {
    Write-Host "Error: Python is not installed or not in PATH"
    exit 1
}

Write-Host "Using Python command: $($pythonCmd.Source)"
& $pythonCmd.Source --version

# Install pip if not available
try {
    & $pythonCmd.Source -m pip --version
}
catch {
    Write-Host "pip not found. Installing pip..."
    Invoke-WebRequest -Uri https://bootstrap.pypa.io/get-pip.py -OutFile get-pip.py
    & $pythonCmd.Source get-pip.py
    Remove-Item get-pip.py
}

# Check if requirements.txt exists
if (Test-Path requirements.txt) {
    Write-Host "Installing dependencies..."
    & $pythonCmd.Source -m pip install -r requirements.txt
}
else {
    Write-Host "Error: requirements.txt not found in the current directory"
    exit 1
}

Write-Host "Loading environment variables..."
if (Test-Path .env) {
    Get-Content .env | ForEach-Object {
        if ($_ -match '^(.+)=(.+)$') {
            $key = $matches[1].Trim()
            $value = $matches[2].Trim()
            [Environment]::SetEnvironmentVariable($key, $value, "Process")
            Write-Host "Set environment variable: $key"
        }
    }
    Write-Host "Environment variables loaded successfully"
}
else {
    Write-Host "Warning: .env file not found"
}

# Check if app.py exists
$appPath = Join-Path -Path $scriptPath -ChildPath "langchain_integration\app.py"
if (Test-Path $appPath) {
    Write-Host "Starting the Flask application..."
    & $pythonCmd.Source $appPath
}
else {
    Write-Host "Error: app.py not found at $appPath"
    exit 1
}