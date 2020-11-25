#! python
# -*- coding: utf-8 -*-

# Секция 1. Импорт библиотек
import csv
import matplotlib.pyplot as plt

# Секция 2.
# тут скачиваем нужные файлы

# Секция 3.


def readCSV(filename, country):
    try:
        with open(filename, encoding='utf-8', newline='') as file:
            # для анализа файла используем класс DictReader
            reader = csv.DictReader(file)
            for line in reader:
                if line['Country/Region'] == country:
                    return line
    except IOError as e:                                            # обработки ошибки чтения
        # вывод ошибки
        return f'Ошибка чтения файла!\n{str(e)}'


confirmed = readCSV('time_series_covid19_confirmed_global.csv', 'Russia')

deaths = readCSV('time_series_covid19_deaths_global.csv', 'Russia')

recovered = readCSV('time_series_covid19_recovered_global.csv', 'Russia')

confirmed_value_lst = []
deaths_value_lst = []
recovered_value_lst = []
timeline_lst = []

for confirmed_key, confirmed_value in confirmed.items():
    for deaths_key, deaths_value in deaths.items():
        for recovered_key, recovered_value in recovered.items():
            if confirmed_key == deaths_key and confirmed_key == recovered_key:
                # print(f'{confirmed_key}: {confirmed_value}, {deaths_value}, {recovered_value}')
                if confirmed_key != 'Province/State' and confirmed_key != 'Country/Region' and confirmed_key != 'Lat' and confirmed_key != 'Long':
                    # print(f'{confirmed_key}: {confirmed_value}, {deaths_value}, {recovered_value}')
                    timeline_lst.append(confirmed_key)
                    confirmed_value_lst.append(confirmed_value)
                    deaths_value_lst.append(deaths_value)
                    recovered_value_lst.append(recovered_value)

# timeline = range(len(confirmed_value_lst))

for i in recovered_value_lst:
    print(i)
print(len(timeline_lst), len(confirmed_value_lst),
      len(deaths_value_lst), len(recovered_value_lst))

plt.title("Зависимости")  # заголовок
# plt.xlabel("x")         # ось абсцисс
# plt.ylabel("y1, y2")    # ось ординат
# plt.grid()              # включение отображение сетки
plt.plot(timeline_lst, deaths_value_lst)
plt.show()
