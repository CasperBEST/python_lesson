# # import sys
#
# # nums_1 = [159, 45, 89]  # список
# # print(sys.getsizeof(nums_1))
# # print(sys.getsizeof(nums_1[0]))
# # print(sys.getsizeof(nums_1[1]))
# # print(sys.getsizeof(nums_1[2]))
# # # print(dir(nums_1))
#
# # nums_2 = (159, 45, 89)  # кортеж не изменяемый, занимает места меньше списка
# # #nums_2[0] = 1
# # #print(dir(nums_2))
# # print(type(nums_2), id(nums_2))
# # print(sys.getsizeof(nums_2))
# # print(sys.getsizeof(nums_2[0]))
# # print(sys.getsizeof(nums_2[1]))
# # print(sys.getsizeof(nums_2[2]))
#
# # print(type(nums_1), id(nums_1))
# # nums_2 = [159, 45, 89]
# # print(type(nums_2), id(nums_2))
# # nums_3 = nums_2.copy()  # nums_3 это тот же спмсок nums_2
# # print(type(nums_3), id(nums_3))
# # nums_3.append('hello')
# # print(nums_2)
#
#
#
# basket = [159.58, 45.81, 81, 89]
# new_items = [24.6, 58.6]
# for el in new_items:
#     basket.append(el)
# print(basket)
# basket.extend(new_items)
# print(basket)
# # basket.append(new_items)
# # print(basket)
# # basket += new_items
# # print(basket)
# # last_item = basket.pop()  # O(1)
# # print(basket)
# # print(last_item)
# # # while basket:
# # #     print(basket.pop())
# # some_item = basket.pop(1)  # O(n)
# # print(some_item)
# # print(basket)
# #
# # basket.insert(2, 155)  # добавление в произвольное место списка O(n)
# # print(basket)
# #
# # basket.remove(58.6)  # удаляет первое значение
# # print(basket)
# # item = 24.6
# # while item in basket:
# #     basket.remove(item)
# # print(basket)
# #
# # basket.reverse()  # разворачиваем список (на месте)
# # print(basket)
# # basket_r = reversed(basket)  # возвращает развернутую копию
# # print(basket_r)
# # for el in basket_r:
# #     print(el)
# # #print(list(basket_r))
# # #print(*basket)
# #
# # q = tuple(basket)
# # print(*q)
#
# print(basket[:3])  # start=0:stop=len:step=1, не включительно, работает с копией
# print(basket[:1000])  # не ломается
# basket_2 = basket[:]  # полная копия
# print(basket[::-1])  # копия развернутого списка
#
# basket_s = sorted(basket, reverse=True)  # сортировка по возрастанию
# print(basket_s)
#
# basket.sort()  # in-place
# print(basket)
#
# print(basket.index(81))  # место в списке
# print(basket.count(24.6))  # кол-во в списке



# msg = 'привет, я обычная строка'
# msg_tmp = list(msg)
# print(msg)
# print(msg_tmp)
# new_msg = '-'.join(msg_tmp)
# print(new_msg)
# #print(dir(msg))
# print(msg.upper())  # lower
# print(msg.split('1'))
# print(msg.strip('!'))
# print('?' + msg + '?')
# print(msg.endswith('!'))  # startswith
# print(msg.count('я'))
# #print(msg.index('я', 'ЯЯЯ'))
# print(msg.index('я', 9))
# print(msg.find('я', 9))
# print(msg.replace('я', 'ю').upper())



# GREETTING = 'Уважаемый {}, поздравляю Вас с {}!'
# party = '1 мая'
# names = ['Иван', 'Сергей', 'Даниил']
# for name in names:
#     #print(GREETTING.format(name, party))
#     #print('Уважаемый %s, поздравляю Вас с %s!' %(name, party))
#     print((f'Уважаемый {name}, поздравляю Вас с {party}!'))
#
# age = 5
# print(f'возраст {age:03d}')
# price = 1564.48756442
# print(f'цена {price:.2f}')
# print(round(price, 5))
# name = 'Иван'



num = input('Enter a number: ')
print(True if num.isdigit() else None)  # тернарный оператор
if num.isdigit():
    print(True)
else:
    print(None)
print(num.isdigit() or None)
print(num.isdigit())
