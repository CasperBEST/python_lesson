def thesaurus_adv(items_adv):
    """ Функция принимающая строки в формате 'Имя Фамилия' и возращающая словарь,
    в котором ключи - первые буквы фамилий"""
    dict_surname = {}  # словарь для заполнения данными
    # создаем ключ по первой букве фамилии и значение из аргумента
    for item_adv in items_adv:
        surname_list = []
        surname = item_adv[item_adv.find(' ') + 1:]  # срез строки по пробелу (отделяем фамилию)
        if dict_surname.get(surname[0]) is None:  # если ключ отсутствует создаем элемент словаря
            surname_list.append(item_adv)
            dict_surname[surname[0]] = surname_list
        else:  # если ключ существует - добавляем значение
            surname_list = dict_surname[surname[0]]
            surname_list.append(item_adv)
            dict_surname[surname[0]] = surname_list
    for key_name in dict_surname:  # создаем из значений словари с ключом первой буквы имени
        list_names = dict_surname[key_name]
        dict_surname[key_name] = thesaurus(list_names)
    return dict_surname


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


names = ("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Илья Пахолков",
         "Альбина Гилязова", "Александр Гаврилко", "Иван Павлов", "Лариса Фурлетова")
result_dict = thesaurus_adv(names)
sorted_result_dict = sorted(result_dict.items(), key=lambda x: x[0])  # сортировка словаря по ключу
for key, value in sorted_result_dict:  # распаковка словаря
    print(key, value)
