#!/usr/bin/python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                             #
#   Cry-Bot developed and maintained by KobyW (Crypher#0001)  #
#                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import discord
from discord.ext import commands
from configparser import ConfigParser
import requests

# Using configparser to fetch token from config.ini
# This prevents the token from being pushed to github 
parser = ConfigParser()
parser.read('./config.ini')
TOKEN = parser.get('ini', 'token')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('\n')
    print('Bot is ready!')
    print('Using discord.py version: ' + discord.__version__)
    print('\n')
    await client.change_presence(activity=discord.Game(name="Under Development - @Crypher#0001"))

@client.event
async def on_command_completion(ctx):
    message = ctx.message 
    emoji = client.get_emoji(764607102378967041)
    await message.add_reaction(emoji)

@client.command()
async def yo(ctx):
    await ctx.send(f'yo. ({round (client.latency * 1000) }ms)')

@client.command()
async def invite(ctx):
    await ctx.send('Crypher.net is the default invite link')

client.run(TOKEN)