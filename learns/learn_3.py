# функуии называются глаголами
# аргументы функции
# именованные аргументы можно указывать в любом порядке, позиционные только по порядку


def sum_numbers(a, b):
    """Sums two numbers if a > b else multiples numbers
    (Это документация функции)"""
    if a > b:
        return a + b
        # print('этот принт не напечатается')
    return a * b


c = sum_numbers(25, 5)
print(c + sum_numbers(35, 5))
print(help(sum_numbers))


def full_s_calc():
    global s_side, s_circle
    r_val = float(input('Укажите радиус: '))
    h_val = float(input('Укажите высоту: '))
    s_side = 3


def ext_func():
    my_var = 0

    #def int_func():
        #nonlocal


def my_f(m):
    m = m.copy()
    m.append(1)
    return m


a = [3]
print(my_f(a))
print(a)


def my_fu(value, a=None):
    if a is None:
        a = []
    a.append(value)
    return a


print(my_fu(56, [1, 2, 3]))
print(my_fu(567))
print(my_fu(45))

# СЛОВАРИ

user_1 = {'Фамилия' : 'Иванов', 'Имя' : 'Иван', 'Отчество' : 'Иванович',
          'Возраст' : 23, 'Рост' : 172}
print(f'Добрый день, {user_1["Имя"]}!')

