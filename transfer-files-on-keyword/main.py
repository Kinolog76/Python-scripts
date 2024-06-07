import os
import shutil
import sys

def transfer_files(source_folder, target_folder, keyword):
    for file in os.listdir(source_folder):
        full_path = os.path.join(source_folder, file)
        if keyword in file:
            shutil.move(full_path, target_folder)
            print(f'File {file} moved to {target_folder}')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    source_folder = sys.argv[1]
    target_folder = sys.argv[2]
    keyword = sys.argv[3]

    transfer_files(source_folder, target_folder, keyword)