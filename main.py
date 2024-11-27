import requests
import os
import sys
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


SHORTENED_LINK_DOMAINS = ['vk.cc']


def shorten_link(token, original_url):
    api_url = 'https://api.vk.com/method/utils.getShortLink'
    params = {
        'access_token': token,
        'url': original_url,
        'v': '5.199',
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    response_data = response.json()

    if 'response' in response_data:
        short_url = response_data['response']['short_url']
        return short_url
    else:
        error_message = response_data['error']['error_msg']
        raise Exception(f"Ошибка API: {error_message}")


def count_clikcs(token, short_link_key, interval='forever', intervals_count=1, extended=0):
    api_url = 'https://api.vk.com/method/utils.getLinkStats'
    params = {
        'access_token': token,
        'key': short_link_key,
        'interval': interval,
        'intervals_count': intervals_count,
        'v': '5.199',
        'extended': extended,
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    response_data = response.json()
    
    if 'response' in response_data:
        return response_data['response']['stats']
    else:
        error_message = response_data['error']['error_msg']
        raise Exception(f"Ошибка API: {error_message}")


def is_shorten_link(oroginal_url):
    parsed_url = urlparse(oroginal_url)
    return parsed_url.netloc in SHORTENED_LINK_DOMAINS


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser('Считает клики по ссылкам')
    parser.add_argument('address', help='Адрес')
    args = parser.parse_args()
    token = os.getenv('VK_TOKEN')
    original_url = args.address

    if is_shorten_link(original_url):
        try:
            short_link_key = original_url.split('/')[-1]
            stats = count_clikcs(token, short_link_key)
            print(f'Количество кликов: {stats}')
        except Exception as e:
            print(f'Ошибка: {e}')
    else:
        try:
            short_link = shorten_link(token, original_url)
            print(f'Была создана сокращенная ссылка: {short_link}')
        except Exception as e:
            print(f'Ошибка: {e}')
            