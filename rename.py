import os

# Set the directory path where the files are located
folder_path = r"C:\Users\sabdh\OneDrive - Mahindra University (1)\Project_3rd year\GIFS\gifs_1"

# List all files in the folder
files = os.listdir(folder_path)

# String to check for in file names and the string to replace it with
string_to_check = "happy"  # Modify as needed
replacement_string = "Happy"  # Modify as needed

# Iterate through each file and rename it if the string is found
for index, file_name in enumerate(files, start=1):
    if string_to_check in file_name:
        # Construct the new file name by replacing the string and adding an index
        new_file_name = file_name.replace(file_name, f"{replacement_string}_{index}")
        # Build the full paths for the old and new file names
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_file_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file_name}' to '{new_file_name}'")
