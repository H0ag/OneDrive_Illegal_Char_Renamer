import os

# Disallowed characters in folder/file names
disallowed_chars = ['<', '>', ':', '/', '\\', '|', '?', '*', '"']

# Directory to process
DIRECTORY = "path/to/your/directory"

# Function to sanitize names by replacing disallowed characters with '-'
def sanitize_name(name):
    for char in disallowed_chars:
        name = name.replace(char, '-')
    return name

# Function to rename items in a directory
for root, dirs, files in os.walk(DIRECTORY):
    open("renamed_files.txt", "a+").write("\n############## FOLDERS ############\n")
    # Rename folders
    for folder_name in dirs:
        if any(char in folder_name for char in disallowed_chars):
            new_folder_name = sanitize_name(folder_name)
            old_folder_path = os.path.join(root, folder_name)
            new_folder_path = os.path.join(root, new_folder_name)
            os.rename(old_folder_path, new_folder_path)
            open("renamed_files.txt", "a+").write(f'Renamed folder: {old_folder_path} -> {new_folder_path}\n')
            print(f'Renamed folder: {old_folder_path} -> {new_folder_path}')
    
    open("renamed_files.txt", "a+").write("\n############## FILES ############\n")
    # Rename files
    for file_name in files:
        if any(char in file_name for char in disallowed_chars):
            new_file_name = sanitize_name(file_name)
            old_file_path = os.path.join(root, file_name)
            new_file_path = os.path.join(root, new_file_name)
            os.rename(old_file_path, new_file_path)
            open("renamed_files.txt", "a+").write(f'Renamed file: {old_file_path} -> {new_file_path}\n')
            print(f'Renamed file: {old_file_path} -> {new_file_path}')