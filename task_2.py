from urllib.parse import urljoin, quote_plus
from urllib.request import urlopen

from lxml.html import fromstring

# файл работает около 2х с половиной минут!
# Генирируем словарь с ключами русский алфавит
DICT_CHAR = dict([(chr(i), []) for i in range(1040, 1072)])
# Создаем необходимые переменные и адреса
URL_BASE = 'https://ru.wikipedia.org'
URL = 'https://ru.wikipedia.org/wiki/{0}'.format(quote_plus('Категория:Животные_по_алфавиту'))
ITEM_PATH = '.mw-category .mw-category-group ul li a'
NEXT_PAGE_PATH = '#mw-pages > a'


def main(url):
    """Функция перебирает html адреса страниц и запускает функции открытия html страниц и парсинга страницы"""
    first_char = ''
    res = ''
    while first_char != 'A':
        list_doc = get_url(url)
        url_next = list_doc.cssselect(NEXT_PAGE_PATH)
        for i in url_next:
            if i.text == 'Следующая страница':
                res = i.get('href')
        url = urljoin(URL_BASE, res)
        list_doc = get_url(url)
        result, first_char = iter_animal(list_doc, DICT_CHAR)


def iter_animal(animal_list, result):
    """Функция парсит названия животных и по первый букве добавляет в итоговый словарь"""
    for elem in animal_list.cssselect(ITEM_PATH):
        try:
            result[elem.text[0]].append(elem.text)
            key_char = elem.text[0]
        except KeyError:
            key_char = elem.text[0]
            continue
    return result, key_char


def get_url(url):
    """Функция принимает url страницы и возвращает html документ"""
    f = urlopen(url)
    list_html = f.read().decode('utf-8')
    list_doc = fromstring(list_html)
    return list_doc


if __name__ == '__main__':
    main(URL)
    # раскомментировать, чтобы посмотреть итоговый словарь
    # print(DICT_CHAR)
    for key, value in DICT_CHAR.items():
        print(f'{key}: {len(value)}')
