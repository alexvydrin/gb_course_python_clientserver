"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def write_order_to_json(item, quantity, price, buyer, date):

    """
    добавление информации в файл json
    :param item: str продукт
    :param quantity: str количество
    :param price: str цена
    :param buyer: str покупатель
    :param date: str дата
    :return:
    """

    # подгрузим JSON-объект
    with open('orders.json', 'r', encoding='utf-8') as file_json:
        data = json.load(file_json)

    # достучимся до списка, который нужно пополнять
    orders = data['orders']
    order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    orders.append(order)

    # сохраним все обратно в файл
    with open('orders.json', 'w', encoding='utf-8') as file_json:
        json.dump(data, file_json, indent=4)


if __name__ == '__main__':
    write_order_to_json('product_1', '100', '50', 'Vasechkin', '01.10.2020')
    write_order_to_json('product_2', '200', '70', 'Petrov', '01.10.2020')
