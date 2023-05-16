#В словаре элементы вызываються по ключу
#Значения в словаре изменяемые
d1 = {'a':7, 'b':8}
d2 = dict(a=7, b=8)
d3 = dict.fromkeys([1,2,3,4,5], 'value')#Словарь со значениями по умолчанию
print(d3)
del d1['b']#Удаляем элемент словаря

price = {'мясо': 300, 'хлеб': 30, 'вода': 50, 'бананы': 150}

##def buy():
##    pay = 0
##    while True:
##        enter = input("Что покупаем ?:\n")
##        if enter == 'end':
##            break
##        pay += price[enter]
##    return pay
##print(buy())
##
##x = price.get('water')

new_price = {}
for i in price:
    new_price[i] = round(price[i] * 0.85, 2)
#print(new_price) 

for key, value in new_price.items():
    print(key,  value)
