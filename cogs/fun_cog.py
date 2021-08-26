"""
Description:
This Cog contains all the events and commands used for fun and hat-tricks.
"""
# IMPORTS
#import [Module/Package]
from random import choice

from discord.ext import commands        # IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
#import schedule  #? Currently Unusued


class FunCog(commands.Cog):
    """Cog for fun/wacky commands & events."""
    def __init__(self, bot):
        """Initializes the cog, passing in a bot to associate itself with."""
        self.bot = bot
    
    @commands.command(name="insult", aliases=["Insult"])
    @commands.guild_only()
    async def insult(self, ctx):
    	"""Insults random users."""
    	#TODO: Implement scheduling.
    	with open("insults.txt", "r") as insults:
    		usr = choice(tuple(member.mention for member in ctx.guild.members))
    		insult = choice(insults.read().splitlines())
    		await ctx.send("{}\n{}".format(usr, insult))


def setup(bot):
    """Adds The Cog To The Client."""
    bot.add_cog(FunCog(bot))
    #! Unimplemented Custom Context (LEAVE COMMENTED!!)
    #bot.insult_ctx = commands.Context(channel=bot.get_channel(CHANNEL))
    #schedule.every(10).seconds.do(FunCog.insult(bot, bot.insult_ctx))
