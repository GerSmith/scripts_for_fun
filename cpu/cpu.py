#! python
# -*- coding: utf-8 -*-

"""Получение информации о процессоре с помощью Python."""

# pip install psutil
import psutil

# количество ядер
print(f'Physical cores: {psutil.cpu_count(logical=False)}')
print(f'Total cores: {psutil.cpu_count(logical=True)}')

# частота CPU
cpufreq = psutil.cpu_freq()
print(f'Max Frequency: {cpufreq.max:.2f} MHz')
print(f'Min Frequency: {cpufreq.min:.2f} MHz')
print(f'Current Frequency: {cpufreq.current:.2f} MHz')

# загрузка CPU
print('CPU Usage Per Core: ')
for i, percent in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f'Core {i}: {percent}%')
print(f'Total CPU Usage: {psutil.cpu_percent()}%')
