import os
import hashlib

def get_file_checksum(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def remove_duplicate_files(folder_path):
    checksums = {}
    duplicates = []

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_checksum = get_file_checksum(file_path)

            if file_checksum in checksums:
                duplicates.append(file_path)
            else:
                checksums[file_checksum] = file_path

    for duplicate_file in duplicates:
        os.remove(duplicate_file)
        print(f"Duplicate removed: {duplicate_file}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing GIF files: ")
    remove_duplicate_files(folder_path)
