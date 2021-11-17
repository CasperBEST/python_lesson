# переводчик чисел от 0 до 10 с английского языка на русский
def num_translate(item):
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
    result = my_dict.get(item, 'This word cannot be translated!')  # ищем перевод по ключу, если нет - сообщаем о
    # невозможности перевода
    return result  # возвращаем результат


word = input('Write, in English, a number from 0 to 10: ')  # запрашиваем число у пользователя
print('The number "' + word + '" in Russian translation:', num_translate(word))  # вызываем функцию и выводим результат
