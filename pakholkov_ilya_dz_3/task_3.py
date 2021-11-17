def thesaurus(items):
    """ Функция принимающая аргумент в виде имен сотрудников и возращающая словарь, где ключ - первая буква имени,
    а значение - список из имен на эту букву """
    dict_names = {}  # словарь для заполнения данными
    # проверяем в цикле на какую букву начинается имя. Если в словаре еще нет такой буквы - создаем ключ и значение,
    # если такая буква есть - дополняем значение новым именем.
    for item in items:
        list_name = []
        if dict_names.get(item[0]) is None:
            list_name.append(item)
            dict_names[item[0]] = list_name
        else:
            list_name = dict_names[item[0]]
            list_name.append(item)
            dict_names[item[0]] = list_name
    return dict_names


# Перечень имен сотрудников
names = ("Михаил", "Анна", "Иван", "Игорь", "Сергей", "Мария", "Петр", "Илья", "Светлана", "Павел")
result_dict = thesaurus(names)
sorted_result_dict = sorted(result_dict.items(), key=lambda x: x[0])  # сортировка словаря по ключу
for key, value in sorted_result_dict:  # распаковка словаря
    print(key, value)
