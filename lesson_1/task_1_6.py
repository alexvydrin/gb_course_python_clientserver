"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО в формате Unicode (utf-8)

например, with open('test_file.txt', encoding='utf-8') as t_f
невыполнение условия - минус балл
"""

import chardet


STRINGS = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w+') as f:
    for string in STRINGS:
        f.write(f'{string}\n')

with open('test_file.txt', 'rb') as t_f:
    for line in t_f:
        print(line)
        s = line.decode('utf-8', 'replace')
        print(s)

# или второй вариант:
# открываю файл, определяю кодировку и перезаписываю файл в кодировке utf-8 а уже потом:
# with open('test_file.txt', encoding='utf-8') as t_f

# попытаться узнать кодировку файла можем так:
raw_data = open('test_file.txt', "rb").read()
result = chardet.detect(raw_data)
char_enc = result['encoding']
# print(char_enc)
# в моем случае выдает: windows-1251

with open('test_file.txt', 'rb') as t_f:
    with open('test_file_utf8.txt', 'w+', encoding='utf-8') as to_file:
        for line in t_f:
            to_file.write(line.decode(char_enc).encode('utf-8').decode('utf-8'))

# читаем уже юникод
with open('test_file_utf8.txt', 'r', encoding='utf-8') as f_f:
    for line in f_f:
        print(line)
