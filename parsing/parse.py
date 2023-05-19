import requests as req
from bs4 import BeautifulSoup #импортировали класс из библиотеки bs4
from time import sleep #импортировали функцию из модуля

#list_card_url = []#список
#Словарь заголовков запроса, нужен чтобы сайт видел что это браузер а не бот
_headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

#Цикл по страницам каталога
for count in range(1, 8):
    sleep(3)#Делаем паузу в работе скрипта, чтобы не заблокировали на сервере
    url = f"https://scrapingclub.com/exercise/list_basic/&page={count}"
    response = req.get(url, headers=_headers)#Получаем ответ от сайта
    ##print(response.text)
    ##print(type(response.text))
    soup = BeautifulSoup(response.text, "lxml")#вместо lxml можно указать html.parser - тоже анализатор html
    #print(soup)#в перменной soup сейчас DOM дерево
    data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")#в data список элементов

    for i in data:
        url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")#get получает атрибут
        name = i.find("h4", class_="card-title").text.replace("\n", "")
        price = i.find("h5").text

        #мульти лайн строка
        print(f'''
        {url_img} 
        {name} 
        {price}
        ''')
        #card_url = "https://scrapingclub.com" + i.find("a").get("href")
        #list_card_url.append(card_url)
        #print(card_url)