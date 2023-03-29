import threading
import requests
import re
import urllib.parse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from main import all_urls, threads, buffer


def extract_other_urls(link):
    # response = requests.get(link).text
    # soup = BeautifulSoup(response, "lxml")
    # links = [w['href'] for w in soup.find_all('a')]

    # Запрос к сайту
    page = requests.get(link)
    # Парсинг HTML-страницы
    soup = BeautifulSoup(page.text, 'html.parser')

    # Поиск всех ссылок
    pages = soup.find_all('a')
    links = []
    # Вывод всех ссылок
    for link in pages:
        links.append(link.get('href'))

    return links


def make_valid_link(url, base):
    return urllib.parse.urljoin(base, url)


def get_pages(url):
    # links = parse_link(url)
    links = extract_other_urls(url)

    count = 0
    # Смотрим все ссылки с данной ссылки
    while count < len(links):
        links[count] = make_valid_link(links[count], url)

        # if links[count] not in buffer:
        #     buffer.append(links[count])

        count += 1
    # возвращаем найденные ссылки
    return links


def generate_links(url):
    # получаем список ссылок на странице
    links = get_pages(url)
    # добавляем в список всех найденных ссылок
    all_urls.extend(links)


def start_threads(link):
    # создаем новый поток
    thread = threading.Thread(target=generate_links, args=(link,))
    # добавляем поток в список
    threads.append(thread)
    # запускаем поток
    thread.start()


def save_data(data, filename):
    # создаем пустой элемент
    root = ET.Element('urlset')
    # перебираем все найденные данные
    for item in data:
        # создаем элемент с тегом url
        url = ET.SubElement(root, 'url')
        # создаем элемент с тегом loc
        loc = ET.SubElement(url, 'loc')
        # добавляем ссылку в loc
        loc.text = item
    # формируем дерево элементов
    tree = ET.ElementTree(root)
    # сохраняем данные в файл
    tree.write(filename)
