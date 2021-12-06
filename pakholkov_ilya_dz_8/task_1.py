import re

PATTERN = r'(?P<username>^[a-z][\w\d.]+)@(?P<domain>[a-z]{4}\.[a-z]{2})'


def email_parse(address):
    """Функция принимает email адрес и возвращает в виде словаря имя пользователя и почтовый домен"""
    result = re.finditer(PATTERN, address)
    for i in result:
        return i.groupdict()


def email_is_valid(name):
    """Проверяет валидность адреса"""
    return re.match(PATTERN, name)


email = input('Введите e-mail адрес:\n')
valid_email = email_is_valid(email)
if email_is_valid(email):
    print(email_parse(email))
else:  # если введенный адрес не совподает с шаблоном - выбрасываем исключение
    msg = f'Неверный адресс: {email}'
    raise ValueError(msg)
