#!/usr/bin/python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                             #
#   Cry-Bot developed and maintained by KobyW (Crypher#0001)  #
#                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import discord
from discord import message
from discord.ext import commands
from configparser import ConfigParser
import random
import requests

## Using ConfigParser() to parse data from config.ini (such as TOKEN and API keys)
parser = ConfigParser()
parser.read('./config.ini')
TOKEN = parser.get('ini', 'token')

parser.read('./config.ini')
StonkAPIKey = parser.get('ini', 'StonkAPIKey')

client = commands.Bot(command_prefix = '.')

## on_ready function executes after bot is ready to receive data from users
@client.event
async def on_ready():
    print('\n')
    print('Bot is ready!')
    print('Using discord.py version: ' + discord.__version__)
    print('\n')
    await client.change_presence(activity=discord.Game(name="Under Development - @Crypher#0001"))

## React with custom-emoji to every valid user command
@client.event
async def on_command_completion(ctx):
    message = ctx.message 
    emoji = client.get_emoji(764607102378967041)
    await message.add_reaction(emoji)

## Ping command to check bot latency
@client.command()
async def yo(ctx):
    await ctx.send(f'`yo. ({round (client.latency * 1000) }ms)`')

## Invite command displays embed with invite-link
@client.command()
async def invite(ctx):
    embed = discord.Embed(
        color = discord.Color.from_rgb(0, 255, 152)
    )
    embed.set_author(name="Cry-Bot", icon_url="https://cdn.discordapp.com/attachments/495477198967406614/764638753129103360/CryBotTempProfPic.PNG")
    embed.add_field(name = "Invite link:", value="The default invite link is [Crypher.net](Crypher.net)", inline=True)
    await ctx.send(embed=embed)

## Bot information command
@client.command()
async def botinfo(ctx):
    embed = discord.Embed(
        title="Bot Information",
        color = discord.Color.from_rgb(0,255,152)
    )
    embed.set_author(name="Cry-Bot", icon_url="https://cdn.discordapp.com/attachments/495477198967406614/764638753129103360/CryBotTempProfPic.PNG")
    embed.add_field(name="Developer:", value="Crypher#0001", inline=True)
    embed.add_field(name="Github Repository:", value="[Click here](https://github.com/KobyW/Cry-Bot)", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def stonk(ctx, message):
    
    
    #CurrentPrice = stonk.price
    #Change = 
    #DayRange = 
    #YearRange = 
    #PERatio = 
    
    embed = discord.Embed(
        title="Stock"
        ##Color red if daily change - green if +
    )
    embed.set_author(name="Cry-Bot", icon_url="https://cdn.discordapp.com/attachments/495477198967406614/764638753129103360/CryBotTempProfPic.PNG")
    embed.add_field(name="Current Price",value=CurrentPrice,inline=False)
    embed.add_field(name="Change",value=Change,inline=False)
    embed.add_field(name="Day Range",value=DayRange,inline=False)
    embed.add_field(name="Year Range",value=YearRange,inline=False)
    embed.add_field(name="PE Ratio",value=PERatio,inline=False)
    embed.add_field(name="Yahoo Finance",value="https://finance.yahoo.com/quote/" + message,inline=False)
    await ctx.send(embed=embed)

@client.command()
async def stonkprofile(ctx, message):
    r = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol='+message+'&token='+StonkAPIKey)
    companyProfile = r.json()
    name = companyProfile['name']
    logo = companyProfile['logo']
    country = companyProfile['country']
    currency = companyProfile['currency']
    exchange = companyProfile['exchange']
    ticker = companyProfile['ticker']
    ipo = companyProfile['ipo']
    marketCap = companyProfile['marketCapitalization']
    shareOutstanding = companyProfile['shareOutstanding']
    weburl = companyProfile['weburl']
    ## Changing embed color to defer CA and US stocks
    red = 0
    blue = 0
    if companyProfile['country'] == 'CA':
        red = 150
    elif companyProfile['country'] == 'US':
        blue = 255

    embed = discord.Embed(
        title=name,
        color = discord.Color.from_rgb(red,10,blue)
    )    
    embed.set_author(name="Cry-Bot", icon_url="https://cdn.discordapp.com/attachments/495477198967406614/764638753129103360/CryBotTempProfPic.PNG")
    embed.set_thumbnail(url=logo)
    embed.add_field(name="Country",value=country,inline=True)
    embed.add_field(name="Currency",value=currency,inline=True)
    embed.add_field(name="Exchange",value=exchange,inline=False)
    embed.add_field(name="Ticker",value=ticker,inline=True)
    embed.add_field(name="IPO date",value=ipo,inline=False)
    embed.add_field(name="Market Cap",value=marketCap,inline=False)
    embed.add_field(name="# Outstanding Shares",value=shareOutstanding,inline=True)
    embed.add_field(name="Webpage",value=weburl,inline=False)
    await ctx.send(embed=embed)


## Joke command "did i ask?"
@client.command()
async def didiask(ctx):
    choice = random.randint(1,5)
    if choice == 1:
        message = "no one asked"
    elif choice == 2:
        message = "I asked :)"
    elif choice == 3:
        message = "absolutely not"
    elif choice == 4:
        message = "not one person asked"
    elif choice == 5:
        message = "I cannot seem to find a single person who asked.."
    await ctx.send(message)

@client.command()
async def debug(ctx, message):
    print(message)
    companyProfile = requests.get('https://finnhub.io/api/v1/stock/profile2?symbol='+message+'&token='+StonkAPIKey)
    print(companyProfile.json())
    companyProfileJson = companyProfile.json()
    await ctx.send('Debug command complete - Check console')

client.run(TOKEN)