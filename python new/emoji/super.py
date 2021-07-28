import asyncio
import random
import requests
from bs4 import BeautifulSoup


def get_random_historical_fact():
    main_page = requests.get('https://www.generatormix.com/random-history-facts')
    soup = BeautifulSoup(main_page.text, 'lxml')
    two = soup.find('div', class_='col-12 tile-block-inner marg-top first')
    three = two.find('blockquote', class_='text-left').text
    return three

print(get_random_historical_fact())