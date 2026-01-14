import discord
from bot_logic import gen_pass

# A variável intents armazena as permissões do bot 
# intent sao permissoes
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)
#client/bot o proprio bot

#async: usado para declarar uma função assíncrona - ele espera a internet para funcionar por exemplo
#await: usado dentro de funções async para esperar o resultado de outra função assíncrona sem travar o restante do programa.
@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'): #startswiht comeca com econtent conteudo - se o conteudo da mensagem comeca com...
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
    if message.content.startswith('!Password'):
        await message.channel.send(f'Sua senha e:{gen_pass(5)}')
    if message.content.startswith('Oii'):
        await message.channel.send(f'Oii {message.author.global_name}')
        await message.channel.send(message.author.avatar)
#f string escreva normal e coloque chave onde precisar
#pode usar o site discord.py para ver um atributo que funciona

client.run('MTQ0MzcwOTkwNTE4NTAxMzgyMA.GpD0Wo.IM_xaE90mch99m3hbU7IdckpkFyh3RPr7PCkn8')
import random
