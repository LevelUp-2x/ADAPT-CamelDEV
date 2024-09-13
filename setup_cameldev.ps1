# Create conda environment
conda create --name adapt-cameldev python=3.10.14 -y;

# Activate the environment
conda activate adapt-cameldev;

# Create a new directory and navigate into it
mkdir ADAPT-CamelDEV-Project;
cd ADAPT-CamelDEV-Project;

# Clone the repository
git clone https://github.com/LevelUp-2x/ADAPT-CamelDEV.git .;

# Print completion message
Write-Host "Setup completed. You are now in the ADAPT-CamelDEV-Project directory with the conda environment 'adapt-cameldev' activated."