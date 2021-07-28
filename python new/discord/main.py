import requests
import discord
import json
import time
from bs4 import BeautifulSoup


def reverse_sentence(sentence):
    final_sentence = str(sentence).split(' ')
    final_sentence.reverse()
    ' '.join(final_sentence)
    return final_sentence


def email_slicer(email):
    main_str = str(email)
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


TOKEN = 'ODQyNzM4Mjg5OTY1NzkzMzYx.YJ5rMQ.CY2S2nv0G7CdOAZ0Og-4FD6CXgA'
PREFIX = '_'
client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(type=discord.ActivityType.watching, name=' _help '))
    print('Bot is ready!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.find(f'{PREFIX}help') != -1:
        embed = discord.Embed(title='This is a Discord bot for showcasing Python utility projects!',
                              description=f'Use the following commands to do different interesting tasks with the bot. Always add a "{PREFIX}" before the command.',
                              color=0x00ff1a)
        embed.add_field(name='Command-1: _hi', value='Greets the user', inline=True)
        embed.add_field(name='Command-2: _email', value='Slices an email into the domain and username', inline=True)
        await message.channel.send(embed=embed)

    if message.content == f'{PREFIX}hi':
        await message.channel.send(f'Hello {message.author}!')

    if message.content.startswith(f'{PREFIX}covid') != -1:
        if message.content.find('intl') != -1:
            await message.channel.send(covid_international())
        elif message.content.find('reg') != -1:
            final_content_rev = str(message.content).replace(f'{PREFIX}covid', '').replace('reg', '').strip()
            await message.channel.send(covid_regional(final_content_rev))

    if message.content.startswith(f'{PREFIX}reverse') != -1:
        final_content_rev = str(message.content).replace(f'{PREFIX}reverse', '').strip()
        if reverse_sentence(final_content_rev) == '':
            return
        elif reverse_sentence(final_content_rev) != '':
            await message.channel.send(reverse_sentence(final_content_rev))

    if message.content.startswith(f'{PREFIX}email') != -1:
        email = str(message.content).replace(f'{PREFIX}email', '').strip()
        await message.channel.send(email_slicer(email))


client.run(TOKEN)
