import discord
from discord.ext import commands
from bot_logic import gen_pass
import os
import random

intent = discord.Intents.default()
intent.message_content = True
bot = commands.Bot(command_prefix='$', intents=intent)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}')

@bot.command() 
async def test(ctx, arg1, arg2, arg3):
    await ctx.send(f'3 arguments: {arg1}, {arg2}, {arg3}')

@bot.command()
async def meme1(ctx):
    with open("image/meme.phyton1.jpeg", 'rb') as meme:
        image = discord.File(meme)
        await ctx.send(file=image)

@bot.command()
async def meme2(ctx):
    with open("image/meme.phyton2.jpg", 'rb') as meme:
        image = discord.File(meme)
        await ctx.send(file=image)

@bot.command()
async def meme3(ctx):
    with open("image/meme.phyton3.jpeg", 'rb') as meme:
        image = discord.File(meme)
        await ctx.send(file=image)

@bot.command()
async def meme(ctx):
    lista_de_memes = os.listdir("C:\Users\diego\OneDrive\Documentos\images")
    meme_aleatorio = random.choice(lista_de_memes)
    with open(f'image/{meme_aleatorio}', 'rb') as meme:
        image = discord.File(meme)
        await ctx.send(file=image)

bot.run('TOKEN')