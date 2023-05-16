import modul_dly_importa as m
#from modul_dly_importa import newf, l#когда из модуля нужна одна функция или переменная
#print(help(modul_dly_importa))
print(dir())
print(m.l)
print(m.newf(2))
'''
Оптимальный вариант импорта это import modul_dly_importa as m
и использовать так import modul_dly_importa.l, m.l
Так не будет путаницы с именами
Модулей много, пользуемся google
'''
print(__name__)

