#! python
# -*- coding: utf-8 -*-

# Свой QR-код на Python

import pyqrcode
# pip install pyqrcode pypng

# QRString = 'https://t.me/python2day'

QRString = 'https://invite.viber.com/?g=JvQyW23oeEqXFUuj4T_Z482yPBPdBrRm'
url = pyqrcode.create(QRString)

url.png('invite_home.png', scale=8)
