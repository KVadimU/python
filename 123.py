import os
spisok = []
for addres, dirs, files in os.walk("d:\\Python"):
##    spisok.append(addres)
    for file in files:
        spisok.append(os.path.join(addres, file))
print(spisok)
