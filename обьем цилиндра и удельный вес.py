import math

PI = math.pi

def radius():
    r = float(input("Введите диаметр цилиндра в см: "))
    r /= 2
    return r
def height():
    h = float(input("Введите высоту цилиндра в см: "))
    return h
    

def volume():
    r = radius()
    h = height()
    s = PI * r ** 2
    v = s * h
    return round(v, 2)
#print(f"Обьем цилиндра равен: {volume()} cм3")
def massa(g):
    m = float(input("Удельный вес г/см3: "))
    return round(m*g/1000, 2)
print(f"Вес цилиндра в кг: {massa(volume())}")
    

