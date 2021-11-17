# Улучшенный переводчик
def num_translate_adv(item):
    """The function translates words from 0 to 10 from English to Russian."""
    # Словарь содержащий числа с переводом
    my_dict = {'zero': 'ноль',
               'one': 'один',
               'two': 'два',
               'three': 'три',
               'four': 'четыре',
               'five': 'пять',
               'six': 'шесть',
               'seven': 'семь',
               'eight': 'восемь',
               'nine': 'девять',
               'ten': 'десять'}
    # проверяем первую букву в слове, если заглавная, то овет тоже даем заглавной
    if item[0].isupper():
        item = item.lower()
        result = my_dict.get(item, 'This word cannot be translated!').title()
    else:
        result = my_dict.get(item, 'This word cannot be translated!')
    return result


word = input('Write, in English, a number from 0 to 10: ')  # запрашиваем число у пользователя
print('The number "' + word + '" in Russian translation:', num_translate_adv(word))  # вызываем функцию
