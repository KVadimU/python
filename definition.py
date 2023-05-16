x = 5
def name():
    x = 100
    return name2(x)#запуск функции name2
def name2(par):
    print(par)
name()

def func():
    x = 10
    def func2():
        nonlocal x
        x = 100
        print(x)
    func2()
    print(x)
func()
print(x)
