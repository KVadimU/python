##l = [1, 2, 3, 4, 5, ["a", "b", "c"]]
##print(l[-1][0])
##print(len(l[5]))
##l[0], l[1] = l[1], l[0]#обмен или свап
##print(l)
##s = list("stroka")
##print(s)
##r = list(range(1, 20))
##print(r)
##for i in r:
##    print(i)
j = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
j.append(2)
j.insert(1, 7)
print(j.count(7))
j.sort()
j.reverse()
e = j.pop(0)#удяляет элемент
j.remove(7)
#j.clear()#очищает список
j.extend(["a", "b"])
k = j.copy()
print(e)
print(j)
print(k)
k.remove("a")
k.remove("b")
#четные элементы
for i in k:
    if i % 2 == 1:
        continue
    print(i)
print(k)
def summa(a, b):
    return a + b
print(summa(2, 3))
