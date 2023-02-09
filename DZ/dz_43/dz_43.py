from bs4 import BeautifulSoup
import requests
import re
import csv

#  # с занятия на счет юникода
#     for i in items:
#         item = i.find("a", class_="fp-item fp-item--2").get("href")
#         sort = i.find("div", class_="item").text.strip()
#         urls = (f"www.garshinka.ru" + item)
#         data = {'url': urls, 'sort': sort}
#         write_csv(data)


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    res = re.sub(r"\D+", "", s)  # str(re.sub(r"\D+", "", s))
    return res


def write_csv(data):
    with open("product.csv", "a", errors="ignore") as f:  # если в строке юникод - errors="ignore"
        writer = csv.writer(f, delimiter=";")
        writer.writerow((data["name"],
                         data["price"],
                         data["product-code"],
                         data["url"]))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    elements = soup.find_all("sd-product-grid-item", class_="product-grid-item")
    for i in elements:
        try:
            name = i.find("a", class_="product-name").text.strip()
        except ValueError:
            name = ""

        try:
            price = i.find("span", class_="main").text.strip()
            price1 = refined(price)
        except ValueError:
            price1 = ""
        try:
            code = i.find("span", class_="code-value").text.strip()
            # code1 = refined(code)
        except ValueError:
            code = ""
        try:
            url = i.find("a", class_="product-name").get("href")
        except ValueError:
            url = ""

        data = {
            "name": name,
            "price": price1,
            "product-code": code,
            "url": url
        }
        write_csv(data)

        print(name)
        print(price1)
        print(code)
        print(url)
    # print(len(elements))


def main():
    url = "https://www.sdvor.com/chelyabinsk/category/bolgarki-ushm-6060"
    get_data(get_html(url))


if __name__ == "__main__":
    main()








# from bs4 import BeautifulSoup
# import requests
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("div", class_="iva-item-content")
#     # print(elements)
#     for i in elements:
#         try:
#             name = i.find("h3", class_="title-root").text
#         except ValueError:
#             name = ""
#
#         print(name)
#     print(len(elements))
#
#
# def main():
#     url = "https://www.avito.ru/chelyabinskaya_oblast/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1&p=1"
#     get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()
