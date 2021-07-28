from bs4 import BeautifulSoup
import requests
import time
from loading_bars import loading_bars


def get_corona_update():
    html_file = requests.get('https://www.worldometers.info/coronavirus/').text
    soup = BeautifulSoup(html_file, 'lxml')
    main_stuff = soup.find_all('div', class_='maincounter-number')
    spans = []
    for x in main_stuff:
        spans.append(x.span.text)
    total_cases = spans[0]
    total_deaths = spans[1]
    total_recovered = spans[2]
    print(f"Total cases: {total_cases}\nTotal Deaths: {total_deaths}\nTotal Recovered: {total_recovered}")


def get_update_by_country(country):
    if str(country).lower() == 'bd':
        html_bd = requests.get('https://www.worldometers.info/coronavirus/country/bangladesh/').text
        soup_bd = BeautifulSoup(html_bd, 'lxml')
        main_bd = soup_bd.find_all('div', class_='maincounter-number')
        main_new_bd = soup_bd.find_all('li', class_='news_li')
        spans = []
        new_cases = []
        new_deaths = []
        for x in main_bd:
            spans.append(x.span.text)
        for y in main_new_bd:
            new_cases.append(str(y.strong).split('strong')[1].replace('>', '').replace('<', '').replace('/', ''))
        for z in main_new_bd:
            new_deaths.append(str(z.text).split(' ')[4])

        new_deaths_bd = new_deaths[0]
        new_cases_bd = new_cases[0].replace('new cases', '')
        total_cases_bd = spans[0]
        total_deaths_bd = spans[1]
        total_recovered_bd = spans[2]
        print(
            f"Bangladesh Stats ---\nTotal Cases: {total_cases_bd}\nTotal Deaths: {total_deaths_bd}\nTotal Recovered: {total_recovered_bd}\nNew Cases: {new_cases_bd}\nNew Deaths: {new_deaths_bd}")
    elif str(country).lower() == 'usa' or str(country).lower() == 'us':
        html_us = requests.get('https://www.worldometers.info/coronavirus/country/us/').text
        soup_us = BeautifulSoup(html_us, 'lxml')
        main_us = soup_us.find_all('div', class_='maincounter-number')
        main_new_in = soup_us.find_all('li', class_='news_li')
        spans = []
        new_cases = []
        new_deaths = []
        for x in main_us:
            spans.append(x.span.text)
        for y in main_new_in:
            new_cases.append(str(y.strong).split('strong')[1].replace('>', '').replace('<', '').replace('/', ''))
        for z in main_new_in:
            new_deaths.append(str(z.text).split(' ')[4])

        new_deaths_us = new_deaths[0]
        new_cases_us = new_cases[0].replace('new cases', '')
        total_cases_us = spans[0]
        total_deaths_us = spans[1]
        total_recovered_us = spans[2]
        print(
            f"USA Stats ---\nTotal Cases: {total_cases_us}\nTotal Deaths: {total_deaths_us}\nTotal Recovered: {total_recovered_us}\nNew Cases: {new_cases_us}\nNew Deaths: {new_deaths_us}")
    elif str(country).lower() == 'india' or str(country).lower() == 'in':
        html_in = requests.get('https://www.worldometers.info/coronavirus/country/india/').text
        soup_in = BeautifulSoup(html_in, 'lxml')
        main_in = soup_in.find_all('div', class_='maincounter-number')
        main_new_in = soup_in.find_all('li', class_='news_li')
        spans = []
        new_cases = []
        new_deaths = []
        for x in main_in:
            spans.append(x.span.text)
        for y in main_new_in:
            new_cases.append(str(y.strong).split('strong')[1].replace('>', '').replace('<', '').replace('/', ''))
        for z in main_new_in:
            new_deaths.append(str(z.text).split(' ')[4])

        new_deaths_in = new_deaths[0]
        new_cases_in = new_cases[0].replace('new cases', '')
        total_cases_in = spans[0]
        total_deaths_in = spans[1]
        total_recovered_in = spans[2]
        print(
            f"India Stats ---\nTotal Cases: {total_cases_in}\nTotal Deaths: {total_deaths_in}\nTotal Recovered: {total_recovered_in}\nNew Cases: {new_cases_in}\nNew Deaths: {new_deaths_in}")
    else:
        print('Invalid Country! Type "help" for a list of available countries')


while True:
    input_user = input(
        'Enter a country name(type "help" for a list of available countries\nOr type "exit" to close the program)\nLeave blank to get worldwide stats.\n\n> ')
    if input_user == '':
        get_corona_update()
        time.sleep(5)

    elif input_user == 'help':
        print(
            f"""\nAvailable countries: Bangladesh[type 'bd'], United States[type 'us' or 'usa'], India[type 'india' or 'in']""")
    elif input_user == 'exit':
        break
    else:
        get_update_by_country(input_user)
        time.sleep(5)
