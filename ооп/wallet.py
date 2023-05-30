#Кошелёк
class Wallet:
    def __init__(self, valuta, name = 'unknown'):#init конструктор он сразу создает обьект с определенными значениями
        if valuta not in ('USD', 'EUR'):
            raise ValueError()
        self.__money = 0.00#self - ссылка на конкретный обьект, __money - приватное поле, инкапсулированное
        self.valuta = valuta
        self.name = name

    def Up_balance(self, howmany):
        self.__money = self.__money + howmany

    def Down_balance(self, howmany):
        if self.__money - howmany < 0:
            print("Недостаточно средств")
            raise ValueError("Недостаточно средств")
        self.__money = self.__money - howmany
    def Info(self):
        print(str(self.__money) +" "+ self.valuta) 

x = Wallet('USD', 'Bill')
y = Wallet('EUR')
x.money = 1000
y.money = 20.00
y.Up_balance(100)
y.Down_balance(20)
x.Info()
y.Info()