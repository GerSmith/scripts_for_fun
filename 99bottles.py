#! python
# -*- coding: utf-8 -*-

BOTTLES = 99

for i in reversed(range(1, BOTTLES + 1)):
    word = ""

    if (i <= 19) and (i >= 11):
        word = " бутылок"
    else:
        if (i % 10) == 1:
            word = " бутылка"
        elif i % 10 in (2, 3, 4):
            word = " бутылки"
        else:
            word = " бутылок"

    print(str(i) + word + " пива на стене,")
    print(str(i) + word + " пива!")
    print("Возьми одну, пусти по кругу!")

    if (i - 1) == 0:
        print("Нет бутылок пива на стене")
