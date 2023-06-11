h = ["https:\\caйт.com", "https:\\caйтишко.com", "https:\\какойтоcaйт.net", "https:\\левыйcaйт.net"]
x = (i.split("\\")[1] for i in h if ".com" in i)#выражение генератор, оно сразу передает первое значение в цикл for,
#при этом опре память не загружаеться большим обьемом
print(next(x))
for i in x:
    print(i)
