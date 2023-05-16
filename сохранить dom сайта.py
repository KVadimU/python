import urllib.request

url_list = ["https://appsumo.com/"]
list_defect = []
list_info = []
#list_znak = ["<", ">"]

try:
    for url in url_list:
        try:
            get_url = urllib.request.urlopen(url)
            list_info.append(get_url.read())
            print(get_url.getcode())
        except Exception:
            list_defect.append(get_url)
            print(f"Ошибка соединения {print(get_url.getcode())}!!!")
            continue
    #print(list_info)
finally:
    r = open("save.txt", 'w')
    for i in list_info:
        string = str(i)
        list_strings = string.split("><")
        for j in list_strings:
            print(f"<{j}>")
            r.write(f"<{j}>\n")
        r.close()
       print("Все сохранено, не смотря ни на что")
