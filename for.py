s = "синхрофазатрон"
for i in s:
    if i == "ф":
        char = i
        continue
    print(i)
else:
    print(f"Мы пропустили {char}")
print("Программа идет дальше")
#--------------------------------

string = "абвгдеёжзклмнопрстъьчшщиыуйя"
value = input("Введите слово: ")
for i in string:
    count = 0
    for j in value:
        if i == j:
            count += 1
    if count > 0:
        print(f"Букв {i} было {count}")
#-------------------------------
#Range
for i in range(1, 10):
    print(i)
