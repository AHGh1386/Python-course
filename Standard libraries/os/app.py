import os

# Get the current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# Create a new directory
new_dir = os.path.join(current_dir, "new_directory")
os.mkdir(new_dir)
print("New Directory created:", new_dir)

# Change the current working directory
os.chdir(new_dir)
print("Current Directory after change:", os.getcwd())

# List all files and directories in the current directory
print("Files and Directories in", os.getcwd())
for item in os.listdir():
    print(item)

# Rename a file or directory
old_file = os.path.join(os.getcwd(), "old_file.txt")
new_file = os.path.join(os.getcwd(), "new_file.txt")
os.rename(old_file, new_file)
print("File renamed from", old_file, "to", new_file)

# Delete a file
os.remove(new_file)
print("File deleted:", new_file)

# Delete a directory
os.chdir(current_dir)
os.rmdir(new_dir)
print("Directory deleted:", new_dir)
