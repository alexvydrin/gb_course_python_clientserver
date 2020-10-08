"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""

import os
import re
import csv
import chardet


def get_data():
    """извлекаем заданную информацию из файлов"""
    # создаем главный список для хранения данных отчета
    # и записываем названия столбцов отчета
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]

    # извлекаем значения соответствующих параметров и помещаем их в отдельные списки
    # (использование дополнительных списков кажется излишним, можно сразу работать с main_data)
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []

    # перебор файлов с данными
    for file in os.listdir('.'):
        if re.match(r'^info.*\.txt$', file):

            # инициализируем значения искомых параметров - если поиск в файле будет неудачным
            _os = {
                "prod": "-",
                "name": "-",
                "code": "-",
                "type": "-"
            }

            # попытаемся узнать кодировку файла
            raw_data = open(file, "rb").read()
            char_enc = chardet.detect(raw_data)['encoding']

            # извлекаем значения параметров из файла
            with open(file, 'r', encoding=char_enc) as file_txt:
                for line in file_txt:
                    try_match = re.match(r'^Изготовитель системы:\s*(.*)$', line)
                    if try_match:
                        _os["prod"] = try_match[1]

                    try_match = re.match(r'^Название ОС:\s*(.*)$', line)
                    if try_match:
                        _os["name"] = try_match[1]

                    try_match = re.match(r'^Код продукта:\s*(.*)$', line)
                    if try_match:
                        _os["code"] = try_match[1]

                    try_match = re.match(r'^Тип системы:\s*(.*)$', line)
                    if try_match:
                        _os["type"] = try_match[1]

            # помещаем значения параметров в отдельные списки
            os_prod_list.append(_os["prod"])
            os_name_list.append(_os["name"])
            os_code_list.append(_os["code"])
            os_type_list.append(_os["type"])

    # из текста задания:
    # "Значения для столбцов также оформить в виде списка и поместить в файл main_data"
    # здесь видимо опечатка - использование дополнительного файла main_data кажется излишним
    for i, _ in enumerate(os_prod_list):
        main_data.append([
            os_prod_list[i],
            os_name_list[i],
            os_code_list[i],
            os_type_list[i]
        ])

    return main_data


def write_to_csv(csv_file):
    """запись в файл csv"""
    _main_data = get_data()
    with open(csv_file, 'w', encoding='utf-8') as final_file:
        writer = csv.writer(final_file)
        for _row in _main_data:
            writer.writerow(_row)


if __name__ == '__main__':

    # В примере строки со значениями пронумерованы
    # мне кажется для формата csv это не совсем корректно, поэтому нумерацию строк делать не стал
    write_to_csv('my_data_report.csv')

    # Проверим результат
    with open('my_data_report.csv', 'r', encoding='utf-8') as f_n:
        F_N_READER = csv.DictReader(f_n)
        for row in F_N_READER:
            print(row)
