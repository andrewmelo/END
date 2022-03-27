from discord import Embed
from discord.ext import commands

from models.laser_and_feelings_model import LAFModel
from database.session_handler import insert_into, select_all_from_table
class CharacterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lc'])
    async def listcharacters(self, ctx):
        """Show list of owned characters."""
        characters = LAFModel.get_characters(ctx.author.id)
        for char in characters:
            print(char.character_name)
            print(char.user_id)
        if characters is None:
            await ctx.send('You don\'t have characters.')
        else:
            pass
    
    @commands.command(aliases=['cc'])
    async def createcharacter(self, ctx, *args):
        """Create new character."""
        await ctx.send(
            'Informe os dados do personagem na ordem com apenas um espaço:\n'
            'nome estilo cargo numero objetivo'
        )

        if len(args) == 5:
            character = LAFModel(
                character_name=args[0],
                style=args[0],
                role=args[0],
                number=args[0],
                goal=args[0],
                user_id=ctx.author.id
            )
            insert_into(character)
            #select_one_from(LAFModel, )
            await ctx.send('Personagem criado')
        else:
            await ctx.send('Faltaram informações, tente novamente.')
        
    @commands.command(aliases=['lac'])
    async def listallcharacters(self, ctx):
        """Show list characters."""
        objs = select_all_from_table(LAFModel)
        for obj in objs:
            print(obj.character_name)
            print(obj.user_id)

def setup(bot):
    bot.add_cog(CharacterCog(bot))
