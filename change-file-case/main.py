import os
import sys

def change_file_case(folder):
    for root, dirs, files in os.walk(folder):
        for file_name in files:
            old_name = os.path.join(root, file_name)
            new_name = os.path.join(root, file_name.lower())
            
            try:
                os.rename(old_name, new_name)
            except PermissionError:
                print(f'Название файла изменить невозможно: {file_name}')
        for dir_name in dirs:
            old_dir_name = os.path.join(root, dir_name)
            new_dir_name = os.path.join(root, dir_name.lower())
            try:
                os.rename(old_dir_name, new_dir_name)
            except PermissionError:
                print(f'Название папки изменить невозможно: {dir_name}')
                
if __name__ == "__main__":
    if len(sys.argv) < 2:
       sys.exit(1)

    folder_path = os.path.abspath(sys.argv[1])
    change_file_case(folder_path)