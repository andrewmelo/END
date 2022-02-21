from config import TOKEN
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

list_of_commands = []
for roots, dir, files in os.walk("cogs"):
    for arquivo in files:
        if arquivo.endswith(".py"):
            list_of_commands.append(os.path.join(roots, arquivo))

for n in range(len(list_of_commands)):
    list_of_commands[n] = list_of_commands[n].replace("/", ".")

for f in list_of_commands:
    bot.load_extension(f[:-3])

bot.run(TOKEN)