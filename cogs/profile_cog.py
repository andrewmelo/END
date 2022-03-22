from discord.ext import commands
from datetime import datetime
from random import randrange
from models.player_model import PlayerModel
from database.session_handler import insert_into
from helpers.player import get_name

from constants import DAILY_CLAIM

class ProfileCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['p'])
    async def profile(self, ctx):
        """Setup or show player profile"""
        player = PlayerModel.get_player(ctx.author.id)
        if not player:
            player = PlayerModel(user_id=ctx.author.id)
            insert_into(player)
        embed = player.show(
            nick=get_name(ctx),
            avatar_url=ctx.author.avatar_url,
            currency=player.checking_account,
            savings=player.savings_account
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=['dr'])
    async def dailyreward(self, ctx):
            player = PlayerModel.get_player(ctx.author.id)
            if player.last_daily_claim is not None:
                last_reward_time = datetime.utcnow() 
                - datetime.fromisoformat(player.last_daily_claim)
            else:
                last_reward_time = DAILY_CLAIM
            if last_reward_time.total_seconds >= DAILY_CLAIM.total_seconds:                
                reward = randrange(10, 100)
                player.last_daily_claim = datetime.utcnow()
                player.checking_account += reward
                insert_into(player)
                await ctx.send(f"You got {reward}")
            elif last_reward_time.total_seconds <= 3600:
                await ctx.send(f"Daily reward not available yet:"
                f" {last_reward_time.total_seconds/60} minutes")
            else:
                await ctx.send(f"Daily reward not available yet:"
                f" {last_reward_time.total_seconds/60/60} hours")


def setup(bot):
    bot.add_cog(ProfileCog(bot))
