#! python
# -*- coding: utf-8 -*-

"""Шифр Виженера.

Шифр Виженера — метод полиалфавитного шифрования буквенного текста с использованием ключевого слова
Этот метод является простой формой многоалфавитной замены.
TODO: добавить ввод через консоль типа $sv.py --mes="message to code" --key="key"
TODO: бавить обработку ошибок
TODO: доработать кодирование по всей ASCII таблице
"""

import math

# Открытый алфавит
Open = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Построение квадрата Виженера
S = []
for i in range(1, len(Open)+1):
    s = Open[i:] + Open[:i]
    S.append(s)

# Вывод
print(Open)
print("-----" * len(Open))
for i in range(len(S)):
    print(S[i])

# Шифрование
key = 'alphatown'
message = 'i need long message to code because army divert troops to east bridge'

# определение индекса букв сообщения
a = []
# сообщение будет кодироваться без пробелов
message = message.replace(' ', '')
for i in range(len(message)):
    a.append(Open.index(message[i]))

print(a)

# определение индекса букв ключа
b = []
for j in range(len(key)):
    for i in range(len(S)):
        if key[j] == S[i][0]:
            print(key[j], ' is in ', i, 'element of S alphabet')
            b.append(i)

print(b)
# расширение длины ключа до длины сообщения
B = b * int(math.ceil(len(a)/float(len(b))))
B = B[:len(a)]
print(B)

# шифрование сообщения
Z = ''
for i in range(len(a)):
    Z = Z + S[a[i]][B[i]]

print(Z)

# вывод результатов работы скрипта
print(key)
print(message)
print(Z)
