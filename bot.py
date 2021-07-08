import random
import asyncio
from discord import Game
from datetime import date
from discord.ext.commands import Bot
from pycbrf import ExchangeRates, Banks

BOT_PREFIX = ("?", "!")
TOKEN = "EnterYourTokenHere"

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='cheer_up',
                brief="Вдохновись на день",
                pass_context=True)
async def cheer_up(context):
    possible_responses = [
        'У тебя все получится!',
        'Улыбнись!',
        'Все будет хорошо)',
        'Скоро новый год и каникулы. Ура!',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='square',
                brief="Возведение числа в квадрат",
                pass_context=True)
async def square(ctx, number: int):
    print(number)
    squared_value = number * number
    await client.say(str(number) + " в квадрате = " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Сдаю КСиИТ"))
    print("Logged in as " + client.user.name)


@client.command(name='dollar',
                brief="Узнать курс доллара на сегодня",
                pass_context=True)
async def dollar():
    today = date.today()
    rates = ExchangeRates(today, locale_en=True)
    answer = rates['USD']
    print(answer[4])
    await client.say("Курс доллара в рублях: " + str(answer[4]))


@client.command(name='test',
                brief="тестовая команда",
                pass_context=True)
async def test(context):
    await client.say(context.message.author.mention + " Test!")


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
