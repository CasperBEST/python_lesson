# создаем список из кубов нечетных чисел от 1 до 1000
my_list = []
i = 0
while i <= 1000:
    i += 1
    if i % 2 == 0:
        continue
    my_list.append(i ** 3)

# Выбираем из списка числа сумма чисел которых делится нацело на 7
# и вычисляем сумму цифр этих чисел
sum_total = 0
for i in my_list:
    sum_element_list = 0
    while i != 0:  # вычисляем сумму цифр каждого числа в списке
        sum_element_list = sum_element_list + i % 10
        i = i // 10
    if sum_element_list % 7 == 0:  # проверяем сумму цифр делением нацело на 7
        sum_total = sum_total + sum_element_list
print('Сумма чисел из списка, сумма цифр которых делится нацело на 7, равна', sum_total)

# К каждому элементу списка добавляем 17 и заного вычисляем сумму
sum_total = 0
for i in my_list:
    new_i = i + 17
    sum_element_list = 0
    while new_i != 0:  # вычисляем сумму цифр каждого числа в списке
        sum_element_list = sum_element_list + new_i % 10
        new_i = new_i // 10
    if sum_element_list % 7 == 0:  # проверяем сумму цифр делением нацело на 7
        sum_total = sum_total + sum_element_list
print('Сумма чисел из списка (+17), сумма цифр которых делится нацело на 7, равна', sum_total)
