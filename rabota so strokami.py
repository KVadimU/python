r = open('d:\Обработки\Структура.txt')
l = r.read()
list_znk = ['.', ';']
for i in list_znk:
    r1 = l.replace(i, '*')#замена
print(r1)
r2 = r1.split()#разбить, join-обьеденить
print(r2)
