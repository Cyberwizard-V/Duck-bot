import discord
from discord.ext import commands
import os
import requests
import json
import random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

my_secret = os.environ['BOT_TOKEN']
prefix = "*"
bot = commands.Bot(command_prefix = '*', intents=intents)

client = discord.Client()

quackMessages = [
    "QUACK QUACK QUACK B!TCH", "QuAcK", "Just quacking around... :duck:",
    "What the quack :duck:", "qUaCk mE", "Duck you", "What in the quackchilly duck", "Suck my big duck"
    ]


@client.event
async def on_ready():
    print("Bread")
def get_quote(quoteobj=""):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0][quoteobj]

    return quote


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + "quack"):
        await message.channel.send(random.choice(quackMessages))
      
    if message.content.startswith(prefix + "shawagay"):
        shawasMessage = "In reality, i'm gay - shawa soup 2022"
        await message.channel.send(shawasMessage)

    if message.content.startswith(prefix + "givemetruth"):
        theAnswers = ["that will never happen", "have patience", "no", "maybe", "don't depend on it", "squidward", "smell some feet, and you will find answers"]
        assCrack = discord.Embed(title="",
                                 color=0xF46036)
        assCrack.add_field(name="Quacks of truth :duck:", value=random.choice(theAnswers))
        await message.channel.send(embed=assCrack)

    if message.content.startswith(prefix + "quote"):
        quote = get_quote("q")
        quoteA = get_quote("a")
        embedVar = discord.Embed(title=":duck: Quote by " + quoteA +
                                 " :duck: ",
                                 color=0x206694)
        embedVar.add_field(name="Author ", value=quoteA, inline=False)
        embedVar.add_field(name="Quote ", value=quote, inline=False)
        await message.channel.send(embed=embedVar)
#@bot.command(pass_context = True)
#async def join(message):
#    channel = message.author.voice.channel
#    await channel.connect()
  
#@bot.command(pass_context = True)
#async def leave(message):
#    await message.voice_client.disconnect()

keep_alive()

client.run(my_secret)
