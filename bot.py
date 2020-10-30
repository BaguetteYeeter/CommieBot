import discord 
from dotenv import load_dotenv
import os
from discord.ext import commands
from saves import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='c!')
def save():
    f = open("saves.py", "w")
    f.write("users = " + str(users) + "\nCommiePoints = " + str(CommiePoints))
    f.close

@bot.event
async def on_ready():
    print("cyka bot ready to hardbass")
    
@bot.command(name='test')
async def test(ctx):
    await ctx.send("да, the bot works, товарищ.")

@bot.command(name="bal")
async def bal(ctx):
    if ctx.message.author.name in users:
        for i in range(0,2):
            if ctx.message.author.name == users[i]:
                await ctx.send("You have " + str(CommiePoints[i]) + " Commie Points")

@bot.command(name="we")
async def we(ctx):
    if ctx.message.author.name in users:
        for i in range(0,2):
            if ctx.message.author.name == users[i]:
                await ctx.send("Good comrade! +1 Commie Points")
                CommiePoints[i] = CommiePoints[i] + 1
                save()
    
bot.run(TOKEN)
