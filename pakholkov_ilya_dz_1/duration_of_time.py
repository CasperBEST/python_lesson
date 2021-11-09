# перевод продолжительности времени, в секундах, в удобоваримое отображение

# запрашиваем у пользователя продолжительность
duration = int(input('Введите продолжительность времени (в секундах): '))
# вычисляем секунды
if duration <= 59:
    print('Промежуток времени равен', duration, 'сек')
# вычисляем минуты и секунды
elif duration <= 3599:
    minutes = duration // 60
    seconds = duration % 60
    print('Промежуток времени равен', minutes, 'мин', seconds, 'сек')
# вычисляем часы, минуты и секунды
elif duration <= 86399:
    hours = duration // 3600
    minutes = duration % 3600 // 60
    seconds = duration % 3600 % 60
    print('Промежуток времени равен', hours, 'час', minutes, 'мин', seconds, 'сек')
# вычисляем дни, часы, минуты и секунды
else:
    days = duration // 86400
    hours = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    seconds = duration % 86400 % 3600 % 60 % 60
    print('Промежуток времени равен', days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
