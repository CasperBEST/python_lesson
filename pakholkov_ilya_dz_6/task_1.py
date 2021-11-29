with open('nginx_logs.txt', encoding='utf-8') as f:  # открываем файл и создаем пустой список
    my_list = []
    for line in f:
        addres = line.split(' ')[0]  # находим в тексте нужную информацию
        requst = line.split(' ')[5]
        r_esours = line.split(' ')[6]
        list_tuple = addres, requst, r_esours,  # упаковываем в кортеж и добавляем в список
        my_list.append(list_tuple)
print(*my_list, sep='\n')  # выводим список построчно
