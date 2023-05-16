import math

PI = math.pi

def radius():
    r = float(input("Введите диаметр цилиндра: "))
    r /= 2
    return r
def height():
    h = float(input("Введите высоту цилиндра: "))
    return h
    

def volume():
    r = radius()
    h = height()
    s = PI * r ** 2
    v = s * h
    return round(v, 2)
print(f"Обьем цилиндра равен: {volume()}")


