#! python
# -*- coding: utf-8 -*-

"""Консольный прогресс бар.

Кроссплатформенный инструмент для создания консольного progress bar'а вызовом одной функции.
Один из самых простых, быстрых, понятных и расширяемых инструментов.
Задавайте цели и следите за прогрессом написания кода.
https://github.com/tqdm/tqdm
"""

from tqdm import tqdm
# pip install tqdm
from time import sleep

for i in tqdm(range(1, 1000)):
    sleep(0.01)
