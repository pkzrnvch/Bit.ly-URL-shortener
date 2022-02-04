import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

load_dotenv()

BITLY_TOKEN = os.getenv('BITLY_TOKEN')


def shorten_link(link):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}'
    }
    payload = {
        'long_url': link
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(link):
    parsed_link = urlparse(link)
    link_hostname_and_path = f'{parsed_link.hostname}{parsed_link.path}'
    url_template = ('https://api-ssl.bitly.com/v4/'
    'bitlinks/{bitlink}/clicks/summary')
    url = url_template.format(bitlink=link_hostname_and_path)
    payload = {
        'unit': 'day',
        'units': -1
    }
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}'
    }
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(link):
    parsed_link = urlparse(link)
    link_hostname_and_path = f'{parsed_link.hostname}{parsed_link.path}'
    url_template = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    url = url_template.format(bitlink=link_hostname_and_path)
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    parser = argparse.ArgumentParser(
    description='Обработка ссылок с помощью Bit.ly'
    )
    parser.add_argument('link', help='Ссылка')
    args = parser.parse_args()
    link = args.link
    if is_bitlink(link):
        try:
            number_of_clicks = count_clicks(link)
            print('Количество переходов по ссылке битли:', number_of_clicks)
        except requests.exceptions.HTTPError:
            print('Введена неверная ссылка')
    else:
        try:
            bitlink = shorten_link(link)
            print(bitlink)
        except requests.exceptions.HTTPError:
            print('Введена неверная ссылка')


if __name__ == '__main__':
    main()
