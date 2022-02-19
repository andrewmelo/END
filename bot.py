import discord
from discord.ext import commands

from config import TOKEN
from rpgtk.core import Dice
from rpgtk.exceptions import DiceException

intents = discord.Intents.default()
intents.reactions = True
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(pass_context=True)
async def roll(ctx, arg):
    try:
        dice = Dice(int(arg))
    except (DiceException, ValueError):
        await ctx.send("Valor inválido.")
        return
    await ctx.send("Resultado: {result}".format(result=dice.roll()))

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

bot.run(TOKEN)