# name = input("Enter your name: ")
# print("Hi,", name)
# print("Hi, " + name)


# age = int(input("Введите ваш возраст: "))
#
# if age <= 25:
#     print('Группа не старше 25')
#     print("даем контент для вас")
# elif age <= 40:
#     print("группа не старше 40")
# elif age <= 60:
#     print("группа не старше 60")
# else:
#     print("группа старше 60")


# to_buy = ['молоко', 'хлеб', 'кефир', 'шоколадка']
# for el in to_buy:
#     print(el)
# for i, el in enumerate(to_buy, 1):
#     print(i, el)
# for i in range(len(to_buy)):
#     print(i +1, to_buy[i])


# num = int(input("Введите число: "))
# while num <= 10:
#     print(num)
#     num +=1



# i = 0
# flag = True
# while flag:
#     print("123")
#     while True:
#         i += 1
#         if i >= 10:
#             flag = False
#             break
#         if i % 2 == 0:
#             continue
#         print(i)
#     print('456')

i = 256
sum = 0
while i != 0:
    sum = sum + i % 10
    i = i // 10
print(sum)