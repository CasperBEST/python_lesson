# Склоняем слово "процент" во фразе "N процентов"

i = 0
while i <= 99:  # Проверяем в цикле на какую цифру заканчивается число и меняем окончание
    i += 1
    if 10 < i < 15:
        print(i, 'процентов')
    elif i % 10 == 1:
        print(i, 'процент')
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(i, 'процента')
    else:
        print(i, 'процентов')
