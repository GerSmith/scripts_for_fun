#! python
# -*- coding: utf-8 -*-

"""Классный фоновый арт для своего проекта с помощью pyfiglet.

У библиотеки огромное количество разных шрифтов и настроек
https://github.com/pwaller/pyfiglet
"""

# pip install pyfiglet
from pyfiglet import Figlet

font_text = Figlet(font='slant')
print(font_text.renderText('Hello Bro!'))
print(font_text.renderText('How are you?'))
