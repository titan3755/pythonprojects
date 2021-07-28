import discord
import pyfiglet
import time
import json
import requests
from bs4 import BeautifulSoup
from discord.ext import commands


def get_quotes():
    get_quotes_main = requests.get('https://zenquotes.io/api/random').text
    json_stuff = json.loads(get_quotes_main)
    quote_main = json_stuff[0]['q']
    author_main = json_stuff[0]['a']
    return f'{quote_main} - {author_main}'


def text_to_ascii(text):
    return pyfiglet.figlet_format(text, justify='center', width=65)


def reverse_sentence(sentence):
    final_sentence = str(sentence).split(' ')
    final_sentence.reverse()
    ''.join(final_sentence)
    return final_sentence


def email_slicer(email_main):
    main_str = str(email_main)
    if '@' in main_str and main_str.endswith('.com') or main_str.endswith('.ch') or main_str.endswith('.us'):
        if '@gmail.com' in main_str or '@googlemail.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: Google\nUsername: {username}"""
        elif '@yahoo.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: Yahoo\nUsername: {username}"""
        elif '@hotmail.com' in main_str or '@outlook.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: Microsoft\nUsername: {username}"""
        elif '@protonmail.ch' in main_str or '@protonmail.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: ProtonMail\nUsername: {username}"""
        elif '@zoho.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: ZohoMail\nUsername: {username}"""
        elif '@aol.com' in main_str or '@aim.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: AOLMail\nUsername: {username}"""
        elif '@gmx.com' in main_str or '@gmx.us' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: GMXMail\nUsername: {username}"""
        elif '@icloud.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: Apple\nUsername: {username}"""
        elif '@yandex.com' in main_str:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: YandexMail\nUsername: {username}"""
        else:
            username_list = list(main_str)
            username = ''.join(username_list[:username_list.index('@')])
            return f"""Domain: Custom Domain\nUsername: {username}"""
    elif '@' in main_str:
        username_list = list(main_str)
        username = ''.join(username_list[:username_list.index('@')])
        return f"""Domain: Unknown\nUsername: {username}"""


def covid_international():
    html_file = requests.get('https://www.worldometers.info/coronavirus/').text
    soup = BeautifulSoup(html_file, 'lxml')
    main_stuff = soup.find_all('div', class_='maincounter-number')
    spans = []
    for x in main_stuff:
        spans.append(x.span.text)
    total_cases = spans[0]
    total_deaths = spans[1]
    total_recovered = spans[2]
    return f"Total cases: {total_cases}\nTotal Deaths: {total_deaths}\nTotal Recovered: {total_recovered}"


def covid_regional(country):
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
        return (
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
        return (
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
        return (
            f"India Stats ---\nTotal Cases: {total_cases_in}\nTotal Deaths: {total_deaths_in}\nTotal Recovered: {total_recovered_in}\nNew Cases: {new_cases_in}\nNew Deaths: {new_deaths_in}")


PREFIX = '_'
client = commands.Bot(command_prefix=f'{PREFIX}', case_insensitive=True)
TOKEN = 'ODQyNzM4Mjg5OTY1NzkzMzYx.YJ5rMQ.CY2S2nv0G7CdOAZ0Og-4FD6CXgA'


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(client.guilds)} servers!'))
    print('Bot is Ready!')


@client.command()
async def helpme(ctx):
    embed = discord.Embed(title='List of bot commands', description='')
    await ctx.send('s')


@client.command()
async def hello(ctx):
    await ctx.send(f'Hi {ctx.author}!')


@client.command()
async def email(ctx, email_main):
    await ctx.send(email_slicer(email_main))


@client.command()
async def covid(ctx, region, country=None):
    if str(region) == 'intl' and country is None:
        await ctx.send(covid_international())
    elif str(region) == 'reg' and country is not None:
        await ctx.send(covid_regional(country))


@client.command()
async def reverse(ctx, sentence_main):
    await ctx.send(reverse_sentence(sentence_main))


@client.command()
async def textascii(ctx, word):
    await ctx.send(f'```{text_to_ascii(word)}```')


@client.command()
async def quote(ctx):
    await ctx.send(f'{get_quotes()}')


client.run(TOKEN)
