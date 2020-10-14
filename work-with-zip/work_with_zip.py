#!C:\Python38\python.exe
# -*- coding: utf-8 -*-

# Работа с zip файлами на python

import zipfile

# путь до файла
file_name = 'my_zipFile.zip'

# Открываем файл в режиме чтения
with zipfile.ZipFile(file_name, mode='r') as zip_file:
    print('Распаковываем файлы...')
    zip_file.printdir()
    zip_file.extractall()
    print('Распаковка прошла успешно!')
