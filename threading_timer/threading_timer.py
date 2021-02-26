#! python
# -*- coding: utf-8 -*-

"""Таймер в Python - позволяет отложить выполнение кода на указанное время."""

import threading

print('Поиск ошибок...')


def check_errors():
    """Поиск ошибок."""
    print('Не удалось найти причину завершения программы! :(')


timer = threading.Timer(5.0, check_errors)
timer.start()
