from datetime import datetime as dt

class Player:
    __LEVEL, __HEALT = 1, 100#Константы, свойтсва класса
    __slots__ = ['__level', '__health', '__born']
    def __init__(self):
        self.__level = Player.__LEVEL#приватные свойтсва, инкапсулированные
        self.__health = Player.__HEALT
        self.__born = dt.now()
    @property#деккоратор. Декораторы нужны когда идет командная разработка
    def lvl(self):#Геттер
        return self.__level
    @lvl.setter
    def lvl(self, num):#Сеттер
        self.__level += num
        if self.__level >= 100: self.__level = 100

x = Player()#Создали игрока

print(x.lvl)
x.lvl = 120#Вызвался сеттер метода lvl
print(x.lvl)