import json
import sys

interests = {}
with open('users.csv', encoding='utf-8') as f1:  # из каждого файла создаем список
    with open('hobby.csv', encoding='utf-8') as f2:
        initials = f1.read().replace(',', ' ').split('\n')
        hobbies = f2.read().split('\n')
        if len(hobbies) > len(initials):  # проверяем длину списков, если пользователей меньше - выходим с кодом 1
            sys.exit(1)
        for i in range(0, len(initials)):  # создаем из списков словарь
            if initials[i] == '':  # пропускаем пустые строки в конце (если есть)
                continue
            if i > len(hobbies) - 1 or hobbies[i] == '':  # если список с увлечениями короче - дополняем словарь
                # значениями None
                n = None
            else:
                n = hobbies[i]
            interests[initials[i]] = n

with open('dict_users_hobby.json', 'w', encoding='utf-8') as f:  # записываем словарь в файл
    json.dump(interests, f)

with open('dict_users_hobby.json', encoding='utf-8') as f:  # проверяем что записалось
    my_dict = json.load(f)

print(my_dict)
