import os
import csv
import requests
from bs4 import BeautifulSoup
from constant import BASE_URL, OUTPUT_DIR, MAX_PAGES


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), OUTPUT_DIR)
if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)


def get_links(alphabet):
    all_words = list()
    
    for page_no in range(1, MAX_PAGES + 1):
        url = f'{BASE_URL}{alphabet}/{page_no}'
        response = requests.get(url)

        if response.status_code == 200:
            bs_obj = BeautifulSoup(response.text, 'html.parser')
            word_list = bs_obj.find('div', {'class': 'sw3o2JSDU4SEB11F3dUQ'}).findAll('li')

            # Unpacking both iterables in a list literal using *
            all_words = [*all_words, *list(word_list)]
        else:
            break
    save_links(alphabet, all_words)


def save_links(alphabet, words):
    file_dir = os.path.join(BASE_DIR, 'links')
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    with open(os.path.join(file_dir, f'{alphabet}.csv'), 'w', encoding='UTF8') as file:
        header = ['word', 'link']
        writer = csv.writer(file)
        writer.writerow(header)

        for wrd in words:
            data = list()
            word = wrd.a.get_text()
            link = wrd.a.attrs['href']
            data = [word, link]

            writer.writerow(data)
