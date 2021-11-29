import sys

with open('users.csv', encoding='utf-8') as f1:  # из каждого файла создаем список (построчно)
    with open('hobby.csv', encoding='utf-8') as f2:
        initials = [line.replace(',', ' ')[: -1] for line in f1]
        hobbies = [line[: -1] for line in f2]
if len(initials) < len(hobbies):  # если список с инициалами короче списка увлечений - выходим с кодом 1
    sys.exit(1)
with open('users_hobby.txt', 'w', encoding='utf-8') as f:  # из полученных списков формируем текст и построчно
    # записываем в файл
    for i in range(0, len(initials)):
        n = i
        if i > len(hobbies) - 1:
            n = 'None'
        else:
            n = hobbies[i]
        text = initials[i] + ': ', n, '\n'
        f.writelines(text)
