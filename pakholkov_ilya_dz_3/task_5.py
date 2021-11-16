from random import choice  # импорт функции выбора случайного слова


def get_jokes(n, flag=False):
    """Функция возвращает n шуток, сформированных из трех случайных слов,
    взятых из трёх списков (по одному из каждого). Если аргумент flag = True, то запрещается повтор в шутках
    (каждое слово может использоваться только один раз)"""
    jokes_list = []
    for i in range(n):  # выбираем по одному слову из списков и формируем строку
        random_index = choice(nouns)
        random_index_1 = choice(adverbs)
        random_index_2 = choice(adjectives)
        joke = f'{random_index} {random_index_1} {random_index_2}'
        if flag:  # Если flag=True проверяем слова шуток на совпадения
            list_2 = joke.split()
            for noun in nouns:
                for fun in list_2:
                    if noun == fun:
                        nouns.remove(noun)

            for adverb in adverbs:
                for fun in list_2:
                    if adverb == fun:
                        adverbs.remove(adverb)

            for adjective in adjectives:
                for fun in list_2:
                    if adjective == fun:
                        adjectives.remove(adjective)
        jokes_list.append(joke)  # добавляем строку в список
    return jokes_list


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
result = get_jokes(n=2, flag=True)
print(result)
