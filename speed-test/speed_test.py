#!C:\Python38\python.exe
# -*- coding: utf-8 -*-

# Свой измеритель скорости интернета на Python

from speedtest import Speedtest
# pip install speedtest-cli

st = Speedtest()

# download_speed = float(str(st.download())[0:2] + '.' + str(round(st.download(), 2))[1]) * 0.125
download_speed = round(st.download()/8388608, 2)
# upload_speed = float(str(st.upload())[0:2] + '.' + str(round(st.upload(), 2))[1]) * 0.125
upload_speed = round(st.upload()/8388608, 2)

print(f'Скорость скачивания: {download_speed} MB/s')
print(f'Скорость загруки: {upload_speed} MB/s')
