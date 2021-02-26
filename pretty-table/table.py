#! python
# -*- coding: utf-8 -*-

"""Вывод таблиц в красивом формате.

https://github.com/jazzband/prettytable
"""

from prettytable import PrettyTable
# pip install prettytable

table = PrettyTable()
table.field_names = ['Name', 'Password', 'Sex', 'Age']
table.add_row(['Bill', 'qwerty', 'Male', 22])
table.add_row(['Ann', 'verystrongpwd', 'Female', 27])
table.add_row(['Den', 'admin', 'Male', 33])

print(table)
