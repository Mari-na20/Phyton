import discord
from discord.ext import commands

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

# COMANDO (com parênteses!)
@bot.command()
async def lixo(ctx):
    with open("image/lixo.jpg", "rb") as tempo:
        image = discord.File(tempo)
        await ctx.send(file=image)

# RODAR BOT
bot.run('MTQ0MzcwOTkwNTE4NTAxMzgyMA.GpD0Wo.IM_xaE90mch99m3hbU7IdckpkFyh3RPr7PCkn8')