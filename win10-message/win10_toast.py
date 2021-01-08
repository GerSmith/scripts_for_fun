#! python
# -*- coding: utf-8 -*-

# Всплывающее уведомление Windows в 3 строчки на Python
# pip install win10toast

import win10toast

toaster = win10toast.ToastNotifier()
toaster.show_toast('Привет от Python!\n'
                   'И библиотеки win10toast!',
                   duration=10)
