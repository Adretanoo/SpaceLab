import requests
from bs4 import BeautifulSoup
import logging

item = 1


def connection_status():
    global item
    url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={item}'
    page = requests.get(url)

    if page.status_code != 200:
        return f'Помилка підключення {page.status_code}'

    logging.info("Починаємо збір даних...")
    runner()
    return "Scraping закінчено"


def parsing(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    parents = soup.find_all('div', class_='caption')

    titles = []
    prices = []
    descriptions = []
    images = []

    for parent in parents:
        title = parent.find('a').get_text(strip=True)
        price = parent.find('h4', class_='price').get_text(strip=True)
        description = parent.find('p', class_='description').get_text(strip=True)
        img = soup.find('img', class_='img-fluid').get('src')

        titles.append(title)
        prices.append(price)
        descriptions.append(description)
        images.append(img)

        print(f"Назва: {title}\nЦіна: {price}\nОпис: {description}\n{'-'*40}\nКартинка: https://webscraper.io{img}")

    return titles, prices, descriptions,images


def runner():
    global item
    while item <= 20:
        url = f'https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={item}'

        try:
            page = requests.get(url)
            page.raise_for_status()
        except requests.RequestException as e:
            logging.error(e)
            print(f"Помилка підключення: {e}")
            break

        parsing(page)
        print(f"Завершено сторінку {item}\n{'='*40}")
        logging.info(f"Завершено сторінку {item}")
        item += 1


print(connection_status())
