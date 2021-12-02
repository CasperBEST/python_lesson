def get_spam(adr_list, value):
    """Функция возвращает ключ словаря по значению"""
    for spam, v in adr_list.items():
        if v == value:
            return spam


with open('nginx_logs.txt', encoding='utf-8') as f:  # открываем файл и создаем пустой список
    my_list = []
    for line in f:
        addres = line.split(' ')[0]  # находим в тексте нужную информацию
        requst = line.split(' ')[5]
        r_esours = line.split(' ')[6]
        list_tuple = addres, requst, r_esours,  # упаковываем в кортеж и добавляем в список
        my_list.append(list_tuple)

addres_dict = {}  # Создаем словарь key = ip адрес, val = кол-во повторений key
for el in my_list:
    ip = el[0]
    if ip in addres_dict:
        addres_dict[ip] += 1
    else:
        addres_dict[ip] = 1
max_val = max(addres_dict.values())  # максимальное значение ключа в словаре
spamer = get_spam(addres_dict, max_val)  # адрес спамера
print(f'IP адрес спамера - {spamer}\nОн отправил {max_val} запросов.')
