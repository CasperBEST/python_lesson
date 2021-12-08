from functools import wraps


def val_checker(verbosity=0):
    def _(callback):
        @wraps(callback)
        def wrapper(*args):
            msg = f'Недопустимое значение {args}'
            if verbosity > 0:
                for el in args:  # если аргумент 0 или меньше - поднимает исключение
                    if el <= 0:
                        raise ValueError(msg)
            result = callback(*args)
            return result
        return wrapper
    return _


@val_checker(1)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(-10))
    help(calc_cube)