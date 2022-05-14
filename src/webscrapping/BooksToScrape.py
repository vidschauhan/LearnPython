# Created by vidit.singh at 14-03-2022

import requests
import bs4
import Scrapper  # My custom class in the same package

base_url = "http://books.toscrape.com/catalogue/page-{}.html"


def scrape_books(url):
    response = Scrapper.get_web_response(url)
    soup = Scrapper.beautify_response(response)
    count = 1
    for item in soup.select(".product_pod"):
        if len(item.select('.star-rating.Two')) > 0:  # If there is space in class name then refer it by using dot[.]
            print(f"{count} :: {item.select('a')[1]['title']}")
            count += 1


if __name__ == '__main__':
    for i in range(1, 51):
        print(f"############################# PAGE {i} ###################################")
        scrape_books(base_url.format(i))
