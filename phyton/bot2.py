import discord
from discord.ext import commands
from bot_logic import gen_pass

intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix='$', intents=intent)
@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command() 
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def senha(ctx):
    await ctx.send(gen_pass(5))

bot.run('MTQ0MzcwOTkwNTE4NTAxMzgyMA.GpD0Wo.IM_xaE90mch99m3hbU7IdckpkFyh3RPr7PCkn8')