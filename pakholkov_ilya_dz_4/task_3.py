from requests import get
import datetime


def currency_rates(text):
    """ Функция принимает в качестве аргумента код валюты и возвращает ее стоимость по отношению к рублю (по данным
    http://www.cbr.ru/scripts/XML_daily.asp) и дату, полученную в ответе сервера."""
    text = text.upper()  # меняем регистр запрошенного кода валюты
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # создаем запрос к API
    content2 = response.content.decode(encoding=response.encoding)
    code_list = []
    val_list = []
    date_list = []
    for el in content2.split('Date="')[1:]:  # Находим в ответе дату
        el = el.split('"')[0]
        date_list.append(el)
    curr_date = datetime.datetime.strptime(date_list[0], '%d.%m.%Y')  # Переводим дату в объект date
    for el in content2.split('<CharCode>')[1:]:  # создаем список кодов валют
        code = el.split('<')[0]
        code_list.append(code)
    for el in content2.split('<Value>')[1:]:  # создаем список значений
        val = el.split('<')[0]
        val_list.append(val)
    currency = dict(zip(code_list, val_list))  # создаем словарь из полученных списков
    curr_float = None
    for i in currency:  # проверяем значение по коду валюты
        if i == text:
            curr = currency[i]
            curr_float = float(curr.replace(',', '.'))  # преобразуем значение в float и добавляем дату
    result = curr_float, curr_date.date()
    return result


# Пример:
print(*currency_rates('usd'))
print(*currency_rates('EUR'))
