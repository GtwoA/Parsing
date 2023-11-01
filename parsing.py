import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36"}

def get_url():

    for count in range(1, 51):

        url = f"http://books.toscrape.com/catalogue/page-{count}.html"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        data = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for i in data:
            card_url = "http://books.toscrape.com/" + "catalogue/"+ i.find("a").get("href")
            yield card_url

def array():
    for card_url in get_url():

        response = requests.get(card_url, headers=headers)

        soup = BeautifulSoup(response.text, "html.parser")

        data = soup.find("article",class_="product_page")

        name = data.find("h1").text

        price = data.find("p",class_="price_color").text[1:7]

        url_img = "http://books.toscrape.com/" + data.find("img").get("src")

        yield name, price, url_img
