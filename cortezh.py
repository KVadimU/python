#Кортежи быстрее в циклах
#Занимают меньше памяти
#Не изменяемый тип.Защищен от изменений
k = (1, 2, 3, 5 ,4, 5)
l = tuple("stroka")
a, b, c, d, e, h = k
print(a, b, c, d, e)
print(type(k))
print(l)
print(k[1:5])#срез
y = []
for i in range(len(k)):
    y.append(k[i] + 3)
print(y)
#Если нужно изменить кортеж#
j = list(k)
j[0] = 20
k = tuple(j)
print(k)
#Методы кортежа#
print(k.count(5))
print(k.index(5))
#К кортежу можно добавить другой кортеж
k += (77, 42)
print(k)
