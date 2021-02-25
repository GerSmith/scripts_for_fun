#! python
# -*- coding: utf-8 -*-

"""Как получить IP адрес любого сайта используя Python."""

import socket

target = 'vk.com'

print(f'IP адрес сайта {target}: {socket.gethostbyname(target)}')
