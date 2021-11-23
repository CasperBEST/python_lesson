# # виртуальное окружение
# # import math
# # import numpy as np
# from math import pi
# from numpy import pi, sin, cos
# # from math import * - так делать ненадо
#
# print(pi)
# print(pi)

# модуль requests

# import requests
#
# responce = requests.get('http://geekbrains.ru')
# print(responce.status_code)  # 200 ok
# content = responce.content.decode(encoding=responce.encoding)
# print(type(content))
# print(type(responce))
# for el in content.split('href="')[1:]:
#     print(el.split('"')[0])

# модуль datatime

import datetime

date_1 = datetime.datetime(year=2021, month=11,
                           day=18, hour=23, minute=5)
print(date_1)
delta_t = datetime.timedelta(days=2, hours=1, minutes=33)
print(date_1 - delta_t)
print(date_1.timestamp())
date_2 = datetime.datetime(year=2018, month=1, day=1)
print(date_2 - date_1)
print(date_1.strftime('%H:%M:%S'))
print(datetime.datetime.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M"))
