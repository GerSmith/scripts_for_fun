#! python
# -*- coding: utf-8 -*-

"""Выключение и перезагрузка ПК с помощью python."""

import os
import sys

restart = input('Do you want to restart your PC? (yes / no): ')

if restart == 'no':
    sys.exit(0)
else:
    os.system('shutdown /r /t 5')
