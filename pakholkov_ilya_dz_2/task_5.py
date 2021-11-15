# создаем список с ценами
prices = [23.84, 785.34, 123, 45.1, 78.11, 753.68, 23.99, 2345, 54.55, 345.87, 876.43, 543.67, 93.47, 360, 240.71]
price_list = []  # список для модифицированных значений цен
for price in prices:
    rub = int(price // 1)  # отделяем рубли и копейки
    kop = int(price % rub * 100)
    rub_str = str(rub) + ' руб '  # переводим в строку с добавлением ед.измерения
    kop_str = str(f'{kop:02d}') + ' коп,'  # добавляем разрядность к копейкам
    new_price = rub_str + kop_str
    price_list.append(new_price)  # формируем новый список
print(' '.join(price_list))  # выводим в строку

# сортируем по возрастанию in-place и добавляем id для доказательства неизменяемости объекта
print(id(prices), 'Не сортированный список', prices)
prices.sort()
print(id(prices), 'Список отсортированный по возрастанию', prices)

# создаем новый список с сортировкой по убыванию
prices_reversed = list(reversed(prices))
print(id(prices_reversed), 'Список отсортированный по убыванию', prices_reversed)

# выводим цены 5 самых дорогих товаров по возрастанию
print(prices[-5:])
