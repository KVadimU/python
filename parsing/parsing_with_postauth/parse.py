from requests import session
from bs4 import BeautifulSoup #импортировали класс из библиотеки bs4
from time import sleep #импортировали функцию из модуля
_headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

work = session()
work.get("https://quotes.toscrape.com/", headers=_headers)
response = work.get("https://quotes.toscrape.com/login", headers=_headers)#перешли на страницу с авторизацией
soup = BeautifulSoup(response.text, "lxml")
token = soup.find("form").find("input").get("value")#get - получает значение атрибута value

data = {"csrf_token":token, "username":111, "password":1234}#словарь

result = work.post("https://quotes.toscrape.com/login", headers=_headers, data=data, allow_redirects=True)
print(result)