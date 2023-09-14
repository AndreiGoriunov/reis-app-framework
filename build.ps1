# Configure the name of the executable file
$exe = "main.exe"
# ========================================
# Do not edit below this line
# ========================================
# Clean up the dist, build, and release folders
Remove-Item -Recurse -Force dist, build, release
Get-ChildItem -Path . -Filter "__pycache__" -Recurse -Directory | Remove-Item -Force -Recurse
pyinstaller --onefile -w -n $exe main.py 
Write-Host "Build complete."

Write-Host "Copying files into 'release' directory..."
# Copy the config directory to the release folder
Copy-Item -Path .\config -Destination .\release\config -Recurse -Force

# Wait for a few seconds (adjust the time as needed)
Start-Sleep -Seconds 3

# Copy the $exe file from .\dist\ to .\release\ folder
Copy-Item -Path .\dist\$exe -Destination .\release\$exe -Force
Write-Host "Complete."