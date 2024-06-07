import os
import sys

def remove_prefix_from_files(prefix_to_remove):
    folder_path = "./"
    # Перебираем все файлы в папке
    for filename in os.listdir(folder_path):
        # Проверяем, что имя файла начинается с указанного префикса
        if filename.startswith(prefix_to_remove):
            # Формируем новое имя файла без этого префикса
            new_filename = os.path.join(folder_path, filename.replace(prefix_to_remove, ""))
            # Переименовываем файл
            os.rename(os.path.join(folder_path, filename), new_filename)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    
    prefix_to_remove = sys.argv[1]
    remove_prefix_from_files(prefix_to_remove)