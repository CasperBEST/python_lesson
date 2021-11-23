from requests import get


def currency_rates(text):
    """ Функция принимает в качестве аргумента код валюты и возвращает ее стоимость по отношению к рублю (по данным
    http://www.cbr.ru/scripts/XML_daily.asp) """
    text = text.upper()  # меняем регистр запрошенного кода валюты
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')  # создаем запрос к API
    content2 = response.content.decode(encoding=response.encoding)
    code_list = []
    val_list = []
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
            curr = currency.get(i)
            curr_float = float(curr.replace(',', '.'))  # преобразуем значение в float
    return curr_float


# Пример:
print(currency_rates('usd'))
print(currency_rates('EUR'))
