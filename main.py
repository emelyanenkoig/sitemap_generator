from datetime import datetime
from src.functions import *
from src.database import *
from loguru import logger
from config import all_urls, threads, buffer


def main():
    url = input("Введите URL адрес: ")
    filename = input("Введите название файла в формате 'filename': ")
    # basename = input("Введите название для базы данных в формате 'filename': ")
    time_1 = datetime.now()

    # Первые ссылки
    links = get_pages(url)
    all_urls.extend(links)

    # Стартует многопоточность
    for link in links:
        start_threads(link)

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    # Сохраняем карту сайта / Создаем базу с URL
    save_data(all_urls, f'sitemaps/sitemap_{filename}.xml')
    save_to_data_base(all_urls, filename)

    # Выводим информацию
    logger.info(f'Список собранных ссылок: {list(set(all_urls))}')
    logger.info(f'Количество собранных ссылок: {len(all_urls)}')
    time_2 = datetime.now()
    logger.info(f'Время работы программы: {time_2 - time_1}')


# Запускаем программу
if __name__ == '__main__':
    main()


