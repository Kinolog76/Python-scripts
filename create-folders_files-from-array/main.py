import os

# ! Укажите путь к папке, в которой хотите создать папки
selected_folder = './test/'
# ! Укажите массив с названиями папок
folders_array = ['test-1', 'test-2', 'test-3', 'test-4', 'test-5']

# Приводим массив к нижнему регистру и заменяем пробелы на дефисы
folders_array = [method.lower().replace(' ', '-') for method in folders_array]


for method in folders_array:
    folder_path = os.path.join(selected_folder, method)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
        method_words = method.replace('-', ' ').capitalize()
        file_path = os.path.join(folder_path, '_index.md')
        
        with open(file_path, 'w') as file:
            # ! Добавляем свои поля
            file.write('---\n')
            file.write(f'h1: "SOME H1"\n')
            file.write(f'title: "SOME TITLE"\n')
            file.write(f'description: "SOME DESCRIPTION"\n')
            file.write('---')
            # ! Добавляем свои поля
        print(f"Создал папку --------------------------- {folder_path}")
    else:
        print(f"{folder_path}")