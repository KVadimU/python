def some():
    with open("text.txt", encoding="utf-8") as r:
        for i in r:
            yield i#yeild - превращает функцию в обьект генератор
l = some()
print(next(l))

for i in some():
    print(i.split())
