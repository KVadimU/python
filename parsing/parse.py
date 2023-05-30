import requests as req
from bs4 import BeautifulSoup #импортировали класс из библиотеки bs4
from time import sleep #импортировали функцию из модуля

#list_card_url = []#список
#Словарь заголовков запроса, нужен чтобы сайт видел что это браузер а не бот
_headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
count = 0
#Загрузка картинок
def download(url):
    global count
    count+=1
    resp = req.get(url, stream=True)#strem потоковая передача картиник, т.е. частями
    name_file = url.split("/")[-1].split("-")[0] + str(count)
    
    r = open("d:\\PythonProject\\parsing\\images\\" + name_file + ".jpg", "wb")#записывать и перезаписывать, b-обрабатывать байты
    #split-разбивает на отдельные строки. [-1] берем последий элемент
    #r строка что бы не ругался на служебные символы
    for value in resp.iter_content(1024*1024):#по 1 мб
        r.write(value)
    r.close()

def get_url():#функция генератор
    #Цикл по страницам каталога
    for count in range(1, 8):
        
        url = f"https://scrapingclub.com/exercise/list_basic/&page={count}"
        response = req.get(url, headers=_headers)#Получаем ответ от сайта
        ##print(response.text)
        ##print(type(response.text))
        soup = BeautifulSoup(response.text, "lxml")#вместо lxml можно указать html.parser - тоже анализатор html
        #print(soup)#в перменной soup сейчас DOM дерево
        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")#в data список элементов

        for i in data:
            #url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")#get получает атрибут
            #name = i.find("h4", class_="card-title").text.replace("\n", "")
            #price = i.find("h5").text

            #мульти лайн строка
            #print(f'''
            #{url_img} 
            #{name} 
            #{price}
            #''')
            #card_url = "https://scrapingclub.com" + i.find("a").get("href")
            #list_card_url.append(card_url)
            #print(card_url)
            
            #Заходим в каждую карточку
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            #list_card_url.append(card_url)
            #print(card_url)
            yield card_url#yield - функция замораживаеться и программа идет дальше, функция генератор
def my_array():
    for card_url in get_url():
        response = req.get(card_url, headers=_headers)#Получаем ответ от сайта
        sleep(1)#Делаем паузу в работе скрипта, чтобы не заблокировали на сервере
        soup = BeautifulSoup(response.text, "lxml")#вместо lxml можно указать html.parser - тоже анализатор html
        data = soup.find("div", class_="card mt-4 my-4")#в data сейчас список html код элементов
        #print(data)
        title = data.find("h3").text
        price = data.find("h4").text
        description = data.find("p").text
        url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        download(url_img)
        #print(f'''
        #{title}
        #{price}
        #{description}
        #{url_img}
        #''')
        yield title, price, description, url_img
