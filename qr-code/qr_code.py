#! python
# -*- coding: utf-8 -*-

# Свой QR-код на Python

import pyqrcode
# pip install pyqrcode pypng

QRString = 'https://t.me/python2day'

url = pyqrcode.create(QRString)

url.png('my_qr.png', scale=8)
