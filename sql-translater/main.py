import os
import sys
from googletrans import Translator

def translate_spanish_to_english(src_path, table_name, translate_from, translate_to, table_language_id):
    translator = Translator()
    dest_path = 'new_bd.sql'
    src_path = f'./{src_path}.sql' 
    # Проверка на наличие файла
    if not os.path.exists(src_path):
        print(f"Файла - {src_path} не существует.")
        return
    
    # Открываем исходный файл для чтения и создаем файл назначения для записи
    with open(src_path, 'r', encoding='utf-8') as src_file, open(dest_path, 'w', encoding='utf-8') as dest_file:
        copy = False
        for line in src_file:
            # Начинаем копирование
            # Если встретили строку с именем нужной таблицы то начинаем копирование и перевод
            if f"INSERT INTO `{table_name}`" in line:
                copy = True
            if copy:
                # Получаем список значений строки
                values_list = line.strip()[1:-1].split(',')
                # Получаем id языка
                language_id = values_list[3].strip()
                # Выполняем перевод если id языка совпадает с id языка, который нужно перевести
                if language_id == table_language_id:
                    parts = line.split("', '")
                    text_index = 1
                    original_text = parts[text_index].strip("'")
                    translated_text = translator.translate(original_text, src=translate_from, dest=translate_to).text
                    parts[text_index] = translated_text
                    line = "', '".join(parts)
                dest_file.write(line)
                if line.strip().endswith(';'):
                    copy = False
            else:
                dest_file.write(line)
                
    # Выводим сообщение если скрипт сработал успешно
    print(f"Перевод c {translate_from} на {translate_to} в таблице {table_name} успешно выполнен.")

if __name__ == "__main__":
    if len(sys.argv) != 6:
        sys.exit(1)
        
    # Получаем аргументы из командной строки
    source_file = sys.argv[1]
    table_name = sys.argv[2]
    translate_from = sys.argv[3]
    translate_to = sys.argv[4]
    table_language_id = sys.argv[5]
    
    # Вызываем функцию
    translate_spanish_to_english(source_file, table_name, translate_from, translate_to, table_language_id)
