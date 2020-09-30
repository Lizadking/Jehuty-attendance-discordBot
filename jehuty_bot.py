import discord
from  discord.ext import commands
"""
File:    jehuty.py
Author:  Lizadking
Date:    9/29/2020
Description:Bot name: Jehuty, Jehuty will provide a basic check in/check out functionality for attendance logging
"""
client = commands.Bot(command_prefix= '!') #refix before each command also client is the instance of the bot
client.remove_command('help') #remove the default help command

@client.event #function decorator
async def on_ready(): #ready up bot
    await client.change_presence(status=discord.Status.online,activity=discord.Game("ZOE2"))
    print("Jehuty activated")

@client.command()
async def ping(ctx): #ctx = context parameter , ping is the command name
    await ctx.send(f'Pong!')

@client.command()
async def checkin(ctx):
    await ctx.channel.purge(limit=1)
    channel = client.get_channel(760542785996193822)# specific channel ID
    await ctx.author.send("You have checked in don't forget to checkout at the end of the meeting")
    user = client.get_user(ctx.author.id)
    await channel.send(f'{user} Checkin complete at: {ctx.message.created_at}')
#checkout function
@client.command()
async def checkout(ctx):
    await ctx.channel.purge(limit=1)
    channel = client.get_channel(760542785996193822)
    await ctx.author.send("You have checked out") #to the user
    user = client.get_user(ctx.author.id)
    await channel.send(f'{user} Checkout complete at: {ctx.message.created_at} enjoy the rest of your day')#to the attnendance log

@client.command()  # A simple command list
async def help_jehuty(ctx):
    embed = discord.Embed \
            (
            title="COMMAND LIST FOR GENERAL USERS",
            description="Here are the commands currently avalible:", color=0xd10a07
        )
    embed.add_field(name="!ping", value="Play a game of Ping-Pong", inline=False)
    embed.add_field(name="!checkin", value="Check in your attendance for the log", inline=False)
    embed.add_field(name="!checkout", value="Checkout your attendance for the log", inline=False)

    await ctx.send(embed=embed)



client.run('') # token of bot

