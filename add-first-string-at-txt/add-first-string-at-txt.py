#! python
# -*- coding: utf-8 -*-
# Скрипт добавляет строку INSERT_STRING в начало текстовых файлов в директории FOLDER_SRC
# и записывает их в FOLDER_MOVE, имя который задаёт пользователь

import os

INSERT_STRING = 'Дарова, пачаны!\n'

FOLDER_SRC = 'many-txt'
FOLDER_MOVE = input(
    'Пожалуйста введите имя директории для изменения файлов (на английском): ')

os.mkdir(FOLDER_MOVE)

list_of_files_to_read = os.listdir(FOLDER_SRC)

for file in list_of_files_to_read:
    try:
        with open(f'./{FOLDER_SRC}/{file}', 'r', encoding='utf-8') as open_src_file:
            content = open_src_file.readlines()
            content.insert(0, INSERT_STRING)
        with open(f'./{FOLDER_MOVE}/{file}', 'w', encoding='utf-8') as open_mv_file:
            open_mv_file.writelines(content)
    except IOError:
        print("Ошибка чтения файла!")
