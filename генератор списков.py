x = [10, 9, 8, 7, 6, 5, 4, 3, 7, 2, 1, 20, -1]
new_l = []
for i in x:
    new_l.append(i*2)
#print(new_l)

#генератор списков, генератор быстрее первого метода в 2 раза
n = [h for h in x if h % 2 == 0 and h > 0]#генератор с условием
m = {i*2 for i in new_l}#множество не содержит дубли
d = {h: h*2 for h in x}#генератор словаря
#print(n)
#print(m)
#print(d)

price = {'meat':2, 'bread':1, 'potato':0.5, 'water': 0.2}
price_new = {i: round(price[i]*0.85, 2)for i in price.keys()}#генератор словаря
print(price_new)

#string1 = "я строка"
#print(string1[0])
