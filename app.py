import discord
import os
from config import TOKEN
from discord.ext import commands
from discord_components import DiscordComponents
from constants import PREFIX

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), intents=intents, help_command=None)
DiscordComponents(bot)

list_of_commands = []
for roots, dir, files in os.walk("cogs"):
    for f in files:
        if f.endswith(".py"):
            list_of_commands.append(os.path.join(roots, f))

for n in range(len(list_of_commands)):
    list_of_commands[n] = list_of_commands[n].replace("/", ".")

for f in list_of_commands:
    bot.load_extension(f[:-3])


bot.run(TOKEN)
