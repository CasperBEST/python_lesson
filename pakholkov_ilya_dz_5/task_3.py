def merg_list(name, item):
    """ Генератор принимает в качестве аргументов два списка
    и возвращает кортежи созданные из элементов этих списков.
    Если количество элементов второго списка меньше чем в первом,
    то элементы заменяются на None.
    """
    for i in range(0, len(name)):
        el_1 = name[i]
        if i >= len(item):
            el_2 = None
        else:
            el_2 = item[i]
        result = (el_1, el_2)
        yield result


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

unification = merg_list(tutors, klasses)
print(type(unification), '\n')  # доказательство генератора
for n in range(1, len(tutors) + 2):  # проверка работы генератора вплоть до истощения (выдает ошибку ...StopIteration)
    print(next(unification))
