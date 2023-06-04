from datetime import datetime as dt

class Player:
    __LEVEL, __HEALTH = 1, 100#Константы, свойтсва класса
    __slots__ = ['__level', '__health', '__born']
    def __init__(self):
        self.__level = Player.__LEVEL#приватные свойтсва, инкапсулированные
        self.__health = Player.__HEALTH
        self.__born = dt.now()
    @property#деккоратор. Декораторы нужны когда идет командная разработка
    def lvl(self):#Геттер
        return self.__level
    @lvl.setter
    def lvl(self, num):#Сеттер
        self.__level += Player.__typeTest(num)
        if self.__level >= 100: self.__level = 100
    @classmethod#этот декоратор нужен для работы с полями самого класса а не экземпляра(обьекта)
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LEVEL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)
    @staticmethod#статичный метод, работает ни с классом ни с экземпляром а просто служебный метод
    def __typeTest(value):#приватный метод
        if isinstance(value, int):#isinstance проверяет значение на тип
            return value
        else:
            raise TypeError("Должен быть int")

Player.set_cls_field(10)
x = Player()#Создали игрока

print(x.lvl)
x.lvl = 120#Вызвался сеттер метода lvl
print(x.lvl)