import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  
intents.members = True          

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'-----------------------------------')
    print(f'¡Bot 24/7 encendido con éxito!')
    print(f'Conectado como: {bot.user}')
    print(f'-----------------------------------')

@bot.command()
async def hola(ctx):
    await ctx.send(f'¡Hola {ctx.author.mention}! Este bot está vivo 24/7. 🚀')

@bot.command()
async def ping(ctx):
    latencia = round(bot.latency * 1000)
    await ctx.send(f'🏓 ¡Pong! Tardé {latencia}ms.')

bot.run(os.environ.get('DISCORD_TOKEN'))