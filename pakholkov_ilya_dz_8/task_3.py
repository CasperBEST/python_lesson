from functools import wraps


def type_loger(callback):
    @wraps(callback)
    def wrapper(*args):
        name_func = callback.__name__
        type_func = type(callback(*args))
        type_args = {}
        for i in args:
            type_args[i] = type(i)
        print(f'{name_func}{type_args}')
        print(f'{name_func}: {type_func}')
        result = callback(*args)
        return result
    return wrapper


@type_loger
def calc_box(x, y):
    """Площадь прямоугольника"""
    return x * y


@type_loger
def colc_circle(r):
    return 3.14 * r ** 2


if __name__ == '__main__':
    print(calc_box(5, 6))
    print(colc_circle(10))
