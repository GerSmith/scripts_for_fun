#! python
# -*- coding: utf-8 -*-

"""
Как получить чёрно-белое изображение с помощью Python
"""
from PIL import Image
# pip install pillow

img = Image.open('photo_2020-11-12_10-41-12.jpg')
black_and_white_image = img.convert('L')
black_and_white_image.save('bw.jpg')
