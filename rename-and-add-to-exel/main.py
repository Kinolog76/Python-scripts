import os
import re
import pandas as pd
import shutil

def process_files(directory, destination_folder):
    # Создаем пустой DataFrame для записи данных
    data = {'Старое название': [], 'Новое название': []}
    df = pd.DataFrame(data)

    # Перебираем все файлы в указанной директории
    for filename in os.listdir(directory):
        # Фильтруем только файлы с нужным паттерном
        if "php_option=com_seyret&Itemid=" in filename:
            # Извлекаем значения Itemid и id с помощью регулярного выражения
            match = re.search(r'Itemid=(\d+)&task=videodirectlink&id=(\d+)', filename)
            if match:
                itemid_value = match.group(1)
                id_value = match.group(2)
                
                # Формируем новое имя файла без расширения
                new_filename = f"emailform-{itemid_value}-{id_value}"
                
                # Полный путь к текущему файлу
                current_path = os.path.join(directory, filename)
                
                # Перемещаем файл
                destination_path = os.path.join(destination_folder, filename)
                shutil.move(current_path, destination_path)

                # Добавляем данные в DataFrame
                df = df._append({'Старое название': filename, 'Новое название': new_filename}, ignore_index=True)

    # Создаем таблицу в формате CSV с разделителем ;
    csv_path = os.path.join(destination_folder, 'files_table.csv')
    df.to_csv(csv_path, index=False, sep=';')
    print(f"\nТаблица с данными о файлах создана: {csv_path}")

# Укажите путь к директории, в которой нужно обработать файлы
directory_path = "./"
# Укажите путь к папке, куда нужно переместить файлы
destination_folder_path = "./gotovo/"
process_files(directory_path, destination_folder_path)
