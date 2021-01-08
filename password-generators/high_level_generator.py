#! python
# -*- coding: utf-8 -*-

# Генератор паролей высокой сложности в несколько строк кода на Python

import random
from string import digits
from string import punctuation
from string import ascii_letters

symbols = digits + punctuation + ascii_letters
sec_random = random.SystemRandom()

password = ''.join(sec_random.choice(symbols) for i in range(15))

print(f'Ваш пароль высокой сложности: {password}')
