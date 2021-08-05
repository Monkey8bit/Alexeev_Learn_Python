class ZeroDivision(Exception):
    pass


try:
    res = 100 / 0
except ZeroDivisionError:
    try:
        raise ZeroDivision("Divisor must be higher than 0.")
    except ZeroDivision as r:
        print(r)
