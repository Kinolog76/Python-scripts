import os
import shutil
import sys

def organize_files(folder_path):
    # Получаем список файлов в указанной папке
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file_name in files:
        # Формируем полный путь к текущему файлу
        file_path = os.path.join(folder_path, file_name)

        # Игнорируем системные файлы и файлы без расширения .md
        if not file_name.startswith("$") and file_name.endswith(".md"):
            # Извлекаем имя файла без расширения
            file_name_without_extension, file_extension = os.path.splitext(file_name)

            # Создаем папку с именем файла (без расширения)
            folder_name = os.path.join(folder_path, file_name_without_extension)
            os.makedirs(folder_name, exist_ok=True)

            # Перемещаем файл в созданную папку
            new_file_path = os.path.join(folder_name, file_name)
            shutil.move(file_path, new_file_path)

            # Переименовываем файл внутри папки (если нужно)
            # Например, добавляем префикс "new_"
            new_file_name = f"_index.md"
            new_file_path_renamed = os.path.join(folder_name, new_file_name)
            os.rename(new_file_path, new_file_path_renamed)

if __name__ == "__main__":
    if len(sys.argv) != 1:
        sys.exit(0)

    organize_files(folder_path = './')