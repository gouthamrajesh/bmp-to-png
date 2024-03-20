import os

def delete_bmp_files(folder_path):
    num_files_deleted = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.bmp'):
                bmp_path = os.path.join(root, file)
                try:
                    os.remove(bmp_path)
                    num_files_deleted += 1
                    print(f"Deleted {bmp_path}")
                except Exception as e:
                    print(f"Failed to delete {bmp_path}: {e}")
    return num_files_deleted

folder_path = "./FOLDER"

# Delete BMP files within the s6 folder
num_s6_files_deleted = delete_bmp_files(os.path.join(folder_path, "s6"))

# Delete BMP files within the s8 folder
num_s8_files_deleted = delete_bmp_files(os.path.join(folder_path, "s8"))

total_files_deleted = num_s6_files_deleted + num_s8_files_deleted
print(f"Total number of BMP files deleted: {total_files_deleted}")
