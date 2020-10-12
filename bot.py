#!/usr/bin/python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                             #
#   Cry-Bot developed and maintained by KobyW (Crypher#0001)  #
#                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import discord
from discord.ext import commands
from configparser import ConfigParser

## Using ConfigParser() to parse data from config.ini (such as TOKEN)
parser = ConfigParser()
parser.read('./config.ini')
TOKEN = parser.get('ini', 'token')

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

client.run(TOKEN)