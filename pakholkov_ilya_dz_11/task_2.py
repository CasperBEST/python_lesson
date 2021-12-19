class MyDivisionError(Exception):
    pass


try:
    num_1 = int(input("Введите число которое будем делить: "))
    num_2 = int(input("Введить делитель: "))
    if num_2 == 0:
        raise MyDivisionError("На ноль делить нельзя!")
except (ValueError, MyDivisionError) as err:
    print(err)
else:
    print(num_1 / num_2)
finally:
    print("Работа завершена")
