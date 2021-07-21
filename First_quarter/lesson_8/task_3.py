from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:  # итерация по аргументам
            print(f"{func.__name__}({arg}: {type(arg)}), function result: {func(arg)}")
            # вывод названия функции, типа ее аргумента, и результата функции с аргументом
    return wrapper


@type_logger  # функция-декоратор
def calc_cube(x):  # декорируемая функция
    return x ** 3


calc_cube(2, 3, 4, 1)
