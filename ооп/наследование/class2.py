from class1 import Verification
from tkinter import Tk, Button

class V2(Verification):#Унаследовались от Verificztion
    #pass#pass-пройти мимо, выполнить пустой код
    def __init__(self, login, password, age):#Переопределили конструктор
        super().__init__(login, password)#Super() -автоматически ищет методы у родителя. в super(Verification, self)- можно явно указать класс
        self.__Save()
        self.age = age

    def __Save(self):#Переопределили родительский метод и дополнили его. Приватный метод
        with open("d:\\PythonProject\\ооп\\наследование\\users.txt") as r:
            for i in r:
                if f"{self.login, self.password}" + "\n" == i:
                    raise ValueError("Такая запись уже есть")
        Verification.Save()
    def Show(self):
        return self.login, self.password

x = V2('Billi', '12345678', 37)
print(x.Show())

#class My_app(Tk):
 #   def __init__(self):
  #      Tk.__init__(self)
   #     self.geometry('400x400')
    #    self.
     #   self.setUI()
    
    #def setUI(self):
     #   Button(self, text='OK').pack()

#root = My_app()
#root.mainloop()