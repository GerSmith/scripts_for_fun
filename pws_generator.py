#! python
# -*- coding: utf-8 -*-

# Простой генератор паролей
import random
# Настройки
PSW_LEN = 12            # Длина пароля
NUM_OF_PERSONS = 10     # Количество генерируемых паролей

def GetPSW(psw_len=6):
    """
    Функция GetPSW возвращает сгенерированный пароль исходя из его длины,
    которая задаётся агрументом psw_len. По умолчанию psw_len = 6
    """
    psw = ''                # Начальный пароль, пустой
    for i in range(psw_len):
        psw = psw + random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    return psw


print(f'Привет! Я простой генератор паролей!Ё\nТы задал длину в {PSW_LEN} символов для {NUM_OF_PERSONS} персон. Держи пароли:')

for i in range(NUM_OF_PERSONS):
    print(GetPSW(PSW_LEN))
