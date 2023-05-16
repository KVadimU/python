while True:
    try:
        enter = float(input("Введите число: "))
        break
    except ValueError:
        print("Произошла ошибка")
    finally:#Блок финали исполняеться всегда,
            #если будет ошибка то финали всеравно сработает
        print("Это финиш")
print("Все норм")
