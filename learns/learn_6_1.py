f_name = 'file.dat'
with open(f_name, 'r+', encoding='UTF-8') as f:  # на дозапись, курсор в конце
    # print('3 А тут есть перевод строки', file=f)
    f.seek(31)
    print(f.tell())
    print(f.read())
    print(f.tell())

# with open('new_file.txt', 'w', encoding='UTF-8') as f:  # на запись, курсор в начале
#     f.write('Привет\n')
#     f.write('Привет')
#     f.writelines(['Идет урок!','Нет перевода строки'])
#     print('А тут есть перевод строки', file=f)
#     print('А тут есть перевод строки', file=f)

# f = open(f_name, 'r', encoding='UTF-8')  # открытие на чтение, курсор в начале файла
# with open(f_name, 'r', encoding='UTF-8') as f1:
#     with open(f_name, 'r', encoding='UTF-8') as f2:
#         rows = f.readline(4)
#         print(rows)
# content = f.read(8)
# print(content)
# rows = content.split('\n')  # не кроссплатформенно
# rows = content.splitlines()  # нет \n
# rows = f.readline(8)  # есть \n
# print(rows)
# for row in f:  # режим генератора, по строкам
#     #print(row, end='')
#     print(row)  # лишние переводы строки
# while True:
#     row = f.readline(8)
#     print(row, end='')
#     if not row:
#         break
# rows = f.readline(4)
# print(row)

# print(type(f))
# print(f)
# print(dir(f))
# print(f.closed)
# f.close()
# print(f.closed)
