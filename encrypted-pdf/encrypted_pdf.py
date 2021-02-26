#! python
# -*- coding: utf-8 -*-

"""Как зашифровать паролем PDF файл с помощью Python."""

from PyPDF2 import PdfFileWriter, PdfFileReader
# pip install pypdf2


def secure_pdf(file: str, password: str):
    """Шифруем переданный pdf-файл заданным паролем."""
    parser = PdfFileWriter()
    pdf = PdfFileReader(file)
    for page in range(pdf.numPages):
        parser.addPage(pdf.getPage(page))
    parser.encrypt(password)
    with open(f'encrypted_{file}', 'wb') as pdf_file:
        parser.write(pdf_file)
    print(f'Создан...encrypted_{file}')


if __name__ == '__main__':
    file = 'secret.pdf'
    password = 'secret'
    secure_pdf(file, password)
