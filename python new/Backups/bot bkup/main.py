import discord
import pyfiglet
import random
import time
import json
import requests
import asyncio
from itertools import cycle
from bs4 import BeautifulSoup
from discord.ext import commands


def date_facts():
    random_num = random.randint(1, 2)
    main_date = requests.get('http://numbersapi.com/random/date').text
    main_year = requests.get('http://numbersapi.com/random/year').text
    if random_num == 1:
        return main_date
    elif random_num == 2:
        return main_year


def num_facts():
    main_num = requests.get('http://numbersapi.com/random/math').text
    return main_num


def trivial_facts():
    main_trivia = requests.get('http://numbersapi.com/random/trivia').text
    return main_trivia


def gayness():
    random_percnt = random.randint(0, 100)
    return random_percnt


def name_gender(name):
    main = requests.get(f'https://api.genderize.io/?name={name}').text
    json_name = json.loads(main)
    inputted_name = json_name["name"]
    gender = json_name["gender"]
    probability = str(round(float(json_name["probability"]) * 100)) + '%'
    return f'Results for name: **{name}**\nGender: **{gender}**\nProbability: **{probability}**'


def flip_coin():
    outcomes = ['heads', 'tails']
    return random.choice(outcomes)


def get_quotes():
    get_quotes_main = requests.get('https://zenquotes.io/api/random').text
    json_stuff = json.loads(get_quotes_main)
    quote_main = json_stuff[0]['q']
    author_main = json_stuff[0]['a']
    return f'{quote_main} - {author_main}'


def text_to_ascii(text):
    return pyfiglet.figlet_format(text, justify='center', width=65)


def reverse_sentence(sentence):
    final_sentence = list(str(sentence)).copy()
    final_sentence.reverse()
    final_str = ''.join(final_sentence)
    return final_str


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


def get_joke():
    joke = requests.get('https://official-joke-api.appspot.com/jokes/ten').text
    rand_num = random.randint(1, 9)
    dict_json = json.loads(joke)
    main = dict_json[rand_num]['setup']
    punchline = dict_json[rand_num]['punchline']
    return f'{main}\n\n**{punchline}**'


PREFIX = '_'
client = commands.Bot(command_prefix=f'{PREFIX}', case_insensitive=True)
client.remove_command('help')
TOKEN = 'ODQyNzM4Mjg5OTY1NzkzMzYx.YJ5rMQ.CY2S2nv0G7CdOAZ0Og-4FD6CXgA'


async def change_status():
    await client.wait_until_ready()
    while not client.is_closed():
        statuses = [f'{len(client.guilds)} servers!', f'{PREFIX}help']
        msgs = cycle(statuses)
        current_status = next(msgs)
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name=current_status))
        await asyncio.sleep(8)


@client.event
async def on_ready():
    print('Bot is Ready!')


@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title='Help', description="Use the '_help <command>' to show more info on a command.",
                          color=ctx.author.color)
    embed.add_field(name='Fun', value='textascii, hello, quote, reverse, ping, joke, nametogender, coinflip, gay',
                    inline=False)
    embed.add_field(name='Utility', value='email, covid, servers', inline=False)
    embed.add_field(name='Moderation', value='warn, kick(Not available!)', inline=False)
    await ctx.send(embed=embed)


@help.command()
async def textascii(ctx):
    embed = discord.Embed(title='Text to ASCII', description='Converts a word to ASCII art', color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_textascii <word>')
    await ctx.send(embed=embed)


@help.command()
async def hello(ctx):
    embed = discord.Embed(title='Hello', description='Says hello to the user mentioning name and ID',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_hello')
    await ctx.send(embed=embed)


@help.command()
async def quote(ctx):
    embed = discord.Embed(title='Quote', description='Returns a random quote along with author of quote',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_quote')
    await ctx.send(embed=embed)


@help.command()
async def reverse(ctx):
    embed = discord.Embed(title='Reverse', description='Returns reverse form of text',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_reverse <text>')
    await ctx.send(embed=embed)


@help.command()
async def ping(ctx):
    embed = discord.Embed(title='Ping', description='Returns pong',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_ping')
    await ctx.send(embed=embed)


@help.command()
async def jumble(ctx):
    embed = discord.Embed(title='Jumble', description='Play a game of word jumble',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_jumble')
    await ctx.send(embed=embed)


@help.command()
async def email(ctx):
    embed = discord.Embed(title='Email', description='Returns the domain and username of a given email address',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_email <emailAddress>')
    await ctx.send(embed=embed)


@help.command()
async def covid(ctx):
    embed = discord.Embed(title='Covid', description="If region is 'intl', returns international covid stats and if "
                                                     "region is 'reg' and the country is mentioned, returns covid "
                                                     "stats of that country",
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_covid <reg> <country>')
    await ctx.send(embed=embed)


@help.command()
async def warn(ctx):
    embed = discord.Embed(title='Warn', description='Warns the user with a mention',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_warn <user> [description]')
    await ctx.send(embed=embed)


@help.command()
async def joke(ctx):
    embed = discord.Embed(title='Joke', description='Returns a joke',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_joke')
    await ctx.send(embed=embed)


@help.command()
async def nametogender(ctx):
    embed = discord.Embed(title='Name to Gender', description='Returns gender based on name',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_nametogender <name>')
    await ctx.send(embed=embed)


@help.command()
async def coinflip(ctx):
    embed = discord.Embed(title='Coin Flip', description='Flip a coin with random outcomes',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_coinflip')
    await ctx.send(embed=embed)


@help.command()
async def gay(ctx):
    embed = discord.Embed(title='Gay', description='Returns your gayness \U0001f642',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_gay <user>')
    await ctx.send(embed=embed)


@help.command()
async def servers(ctx):
    embed = discord.Embed(title='Servers', description='Returns the number of servers bot is in',
                          color=ctx.author.color)
    embed.add_field(name='cmdSyntax', value='_servers')
    await ctx.send(embed=embed)


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
    real_sentence = str(ctx.message.content).replace(f'{PREFIX}reverse', '').strip()
    await ctx.send(reverse_sentence(real_sentence))


@client.command()
async def textascii(ctx, word):
    await ctx.send(f'```{text_to_ascii(word)}```')


@client.command()
async def quote(ctx):
    await ctx.send(f'{get_quotes()}')


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def servers(ctx):
    await ctx.send(f'Bot is in {len(client.guilds)} servers!')


@client.command()
async def coinflip(ctx):
    await ctx.send(f'Coin flipped!\nOutcome: {flip_coin()}')


@client.command()
async def joke(ctx):
    await ctx.send(get_joke())


@client.command()
async def nametogender(ctx, name):
    name_main = str(ctx.message.content).replace(f'{PREFIX}nametogender', '').strip().replace(' ', '')
    await ctx.send(name_gender(name_main))


@client.command()
async def gay(ctx, user=None):
    gayper = gayness()
    if user is None:
        if gayper >= 50:
            await ctx.send(f"You are {gayper}% gay! Wow, that's very gay")
        elif gayper < 50:
            await ctx.send(f"You are {gayper}% gay! Not as gay as I expected...")
    elif user is not None and str(user).find('@') != -1 and str(user).find('@everyone') == -1 and str(user).find(
            '@here') == -1:
        await ctx.send(f"{ctx.message.mentions[0].name} is {gayper}% gay!")


@client.group(invoke_without_command=True)
async def fact(ctx):
    embed = discord.Embed(title='Facts', description='Get random facts about different stuff', color=ctx.author.color)
    embed.add_field(name='Facts relating to dates and time', value='_fact date')
    embed.add_field(name='Facts relating to numbers', value='_fact num')
    embed.add_field(name='Facts relating to trivia', value='_fact trivia')
    await ctx.send(embed=embed)


@fact.command()
async def date(ctx):
    await ctx.send(date_facts())


@fact.command()
async def num(ctx):
    await ctx.send(num_facts())


@fact.command()
async def trivia(ctx):
    await ctx.send(trivial_facts())


@client.command()
async def purge(ctx, amount=20):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Deleted {amount} messages!')

client.loop.create_task(change_status())
client.run(TOKEN)
