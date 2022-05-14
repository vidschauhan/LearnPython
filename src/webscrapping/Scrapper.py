# Created by vidit.singh at 11-03-2022
import requests
import bs4

dir_location = "D:\\Data Engineering\\Udemy - 2021 Complete Python Bootcamp From Zero to Hero in Python\\Udemy - 2021 " \
               "Complete Python Bootcamp From Zero to Hero in Python\\"


def get_web_response(url):
    return requests.get(url)


def beautify_response(content1):
    return bs4.BeautifulSoup(content1.text, "lxml")


def scrap_data(soup, class_name):
    for text in soup.select(class_name):
        print(text.text)


def scrap_image(soup, class_name):
    for text in soup.select(class_name):
        for i in text.select('.image'):
            image_url = i.contents[0]['src']
            print(image_url)
            yield requests.get("https:" + image_url)


def save_image(image_list, file_name, extension):
    from random import random
    for image_binary in image_list:
        file = open(dir_location + file_name + str(random()) + extension, "wb")
        file.write(image_binary.content)


if __name__ == "__main__":
    content = get_web_response("https://en.wikipedia.org/wiki/IPad_Pro")
    sop = beautify_response(content)
    scrap_data(sop, '.toctext')
    lists = scrap_image(sop, '.infobox-image')
    save_image(lists, "Ip", ".png")
