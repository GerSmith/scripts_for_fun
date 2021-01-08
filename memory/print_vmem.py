#! python
# -*- coding: utf-8 -*-

"""
Как узнать сколько используется оперативной памяти с помощью Python
"""

import psutil
# pip install psutil


def get_size(bytes, suffix='B'):
    """
    Функция принимает значение байт и приводит их в
    читабельное значение - Кб, Мб, Гб...
    """
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes: .2f}{unit}{suffix}'
        bytes /= factor


vmem = psutil.virtual_memory()
print(f'Всего: {get_size(vmem.total)}')
print(f'Доступно: {get_size(vmem.available)}')
print(f'Используется: {get_size(vmem.used)}')
print(f'Используется в процентах: {vmem.percent}')
