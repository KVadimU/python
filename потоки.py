x = input("Введите число: ")
if x == str:
    x = 1
    print("x был строкой")
elif not x == float:
    int(x)
    print("x был с плавоющей точкой")
    r = x * 2
    print(r)
