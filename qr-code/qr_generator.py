#! python
# -*- coding: utf-8 -*-

"""Генератор QR-кодов."""

# pip install qrcode
import qrcode

url = "https://www.youtube.com/c/PythonToday/videos"

img = qrcode.make(url)
img.save("p2d.png")
print("[+] QR code done")
