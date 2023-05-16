import requests as req
from bs4 import BeautifulSoup #импортировали класс из библиотеки bs4

url = "https://scrapingclub.com/exercise/list_basic/"
response = req.get(url)#Получаем ответ от сайта
##print(response.text)
##print(type(response.text))
soup = BeautifulSoup(response.text, "lxml")#вместо lxml можно указать html.parser - тоже анализатор html
#print(soup)#в перменной soup сейчас DOM дерево
data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")#в data список элементов

for i in data:
    url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")#get получает атрибут
    name = i.find("h4", class_="card-title").text.replace("\n", "")
    price = i.find("h5").text

    print(f'''#мульти лайн строка
    {url_img} 
    {name} 
    {price}
    ''')