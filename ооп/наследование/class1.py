class Verification:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__LenPassword()
    def __LenPassword(self):#инкапсулированный метод
        if len(self.password) < 8:
            raise ValueError("Слабый пароль")
    def Save(self):
        with open('d:\\PythonProject\\ооп\\наследование\\users.txt', 'a') as r:#With - обработка ошибок
            r.write(f"{self.login, self.password}" + "\n")