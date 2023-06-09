def decor(f):#f - ссылка на функцию make
    def wrapper():#функция обертка
        print("Код декоратора")
        f()
        print("Второй код декоратора")
    return wrapper

@decor #make = decor(make)
def make():
    s = input("Напишите что нибудь...")
    print(s)
#x = make
#x()
make()
