# SQL переводчик

## Запуск скрипта

1. Создаем папку в которой будем выполнять скрипт
2. В папку помещаем **main.py** и **.sql** файл в котором нужно перевести данные
3. Открываем терминал и переходим в папку с файлом
4. Устанавливаем библиотеку _googletrans_:

```
pip install googletrans
```

5. Ваша структура таблицы **_'translates'_** должна выглядеть так:

```sql
INSERT INTO `translates` (`id`, `title`, `text`, `language_id`, `created_at`, `updated_at`, `link`) VALUES
(1, 'about', 'About', 2, '2024-02-16 10:40:32', '2024-02-16 10:40:32', NULL),
(2, 'get_started', 'Get Started', 2, '2024-02-16 10:40:32', '2024-02-16 10:40:32', NULL),
(3, 'lets_go', 'Let`s Go', 2, '2024-02-15 10:40:32', '2024-02-15 10:40:32', NULL),
```

6. Для запуска скрипта в терминале пишем:
```
python main.py source_file table_name translate_from translate_to table_language_id
```
   **Где:**
- `source_file` - название вашего SQL файла
- `table_name` - название таблицы которую нужно перевести
- `translate_from` - язык с которого нужно перевести
- `translate_to` - язык на который нужно перевести
- `table_language_id` - id языка в таблице

**По итогу команда запуска скрипта будет выглядеть так:**
```
python main.py my_bd translates en ru 2
```
