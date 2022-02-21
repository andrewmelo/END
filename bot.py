import discord
from discord.ext import commands
from commands_folder.dice_commands import DiceComm
from config import TOKEN

intents = discord.Intents.default()
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

bot.add_cog(DiceComm(bot))

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

bot.run(TOKEN)