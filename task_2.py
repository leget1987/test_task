# Task 2:
# В нашей школе мы не можем разглашать персональные данные пользователей, но чтобы преподаватель и ученик смогли
# объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш),
# мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного,
# имени животного и двузначной цифры. В итоге получается, например, "Перламутровый лосось 77".
# Для генерации таких имен мы и решали следующую задачу:
# Получить с русской википедии список всех животных (Категория:Животные по алфавиту) и вывести количество животных
# на каждую букву алфавита. Результат должен получиться в следующем виде:
# А: 642
# Б: 412
# В:....
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urljoin, quote, quote_plus

from lxml.html import fromstring


URL_BASE = 'https://ru.wikipedia.org'
URL = 'https://ru.wikipedia.org/wiki/{0}'.format(quote_plus('Категория:Животные_по_алфавиту'))
ITEM_PATH = '.mw-category .mw-category-group ul li a'
NEXT_PAGE_PATH = '#mw-pages > a'
#mw-pages > a:nth-child(4)

# result = {}
# result_list = []


# def pars_animal():
#
#     f = urlopen(URL)
#     list_html = f.read().decode('utf-8')
#     list_doc = fromstring(list_html)
#     for elem in list_doc.cssselect(ITEM_PATH):
#         if elem.text[0] not in result:
#             result_list = []
#         result_list.append(elem.text)
#         result[elem.text[0]] = result_list
#     print(result_list)
#     url = list_doc.cssselect(NEXT_PAGE_PATH)[0].get('href')
#     url = urljoin(URL_BASE, url)
#     f_next = urlopen(url)
#     list_html = f_next.read().decode('utf-8')
#     list_doc = fromstring(list_html)
#     #url = list_doc.cssselect(NEXT_PAGE_PATH)[0].get('href')
#     url = list_doc.cssselect(NEXT_PAGE_PATH)
#     for i in url:
#         if i.text == 'Следующая страница':
#             res = i.get('href')
#             print(res)
#             return res
#

def iter_animal(animal_list, result, result_list):
    for elem in animal_list.cssselect(ITEM_PATH):
        if elem.text[0] not in result:
            result_list = []
        result_list.append(elem.text)
        result[elem.text[0]] = result_list
    return result, result_list


def pars_animal(url):
    result = {}
    result_list = []
    res = ''
    while True:
        # f = urlopen(url)
        # list_html = f.read().decode('utf-8')
        # list_doc = fromstring(list_html)
        list_doc = get_url(url)
        result, result_list = iter_animal(list_doc, result, result_list)
        # while True:
        #     url_next = list_doc.cssselect(NEXT_PAGE_PATH)
        #     for i in url_next:
        #         if i.text == 'Следующая страница':
        #             res = i.get('href')
        #     url = urljoin(URL_BASE, res)
        #     list_doc = get_url(url)
        #     result, result_list = iter_animal(list_doc, result, result_list)
        #     return result, result_list
        print(result)
        print(result_list)
        return result, result_list


def get_url(url):
    f = urlopen(url)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)
    return list_doc


pars_animal(URL)




# a = {1: "one", 2: "two", 3: "three"}
# for key, value in a.items():
#     print(key, ":", value)
#
# 1 : one
# 2 : two
# 3 : three