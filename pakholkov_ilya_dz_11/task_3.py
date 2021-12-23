class Validator(Exception):
    pass


my_list = []
while True:
    print("Для остановки введите - stop")
    try:
        number = input("Введите число: ")
        if number.isdigit():
            my_list.append(number)
        elif number == 'stop':
            break
        else:
            raise Validator("Нужно вводить только числа!")
    except Validator as err:
        print(err)
print("Список введенных чисел:", my_list)
