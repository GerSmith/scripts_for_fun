#! python
# -*- coding: utf-8 -*-

"""Генератор армейских цитат."""

import random
import sys

# Открываем файл с базой цитат
try:
    with open('quotes.txt', encoding='utf-8', newline='') as fileQuotes:
        quotesLst = []
        for line in fileQuotes:
            quotesLst.append(line)
except IOError as e:                                            # обработки ошибки чтения
    print(f'Ошибка чтения файла!\n{str(e)}')                    # вывод ошибки
    sys.exit(0)

# Выбираем случайный индекс из списка
quoteIndex = random.randint(0, len(quotesLst))
# Печатаем в консоль случайную цитату
print(quotesLst[quoteIndex])
