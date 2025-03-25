import os

# Path to the folder
full_path = r"C:/Users/racco/Documents/python_project/braintumordetection/archive/"

# Check if the folder is accessible
if os.access(full_path, os.R_OK):
    print("Folder is accessible!")
    print(os.listdir(full_path))
else:
    print(f"Permission denied for {full_path}")
