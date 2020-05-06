#!python
# -*- coding: utf-8 -*-

# Секция 1. Импорт библиотек
import csv
import sys

# Секция 2. 
# тут скачиваем нужные файлы

# Секция 3.
# тут производим обработку нужных файлов
try:
    with open('time_series_covid19_confirmed_global.csv', encoding='utf-8', newline='') as file:
        # для анализа файла используем класс DictReader
        reader = csv.DictReader(file)                           
        for line in reader:
            if line['Country/Region'] == 'Russia':
                print(line)
            
except IOError as e:                                            # обработки ошибки чтения
    print(f'Ошибка чтения файла!\n{str(e)}')                    # вывод ошибки
    sys.exit(0)

