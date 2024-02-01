import random
import time
import discord
from discord.ext import commands

random.seed(time.time())


class Flip(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Choose a random answer")
    async def random(self, ctx, n: int) -> None:
        choice = random.randint(1, n)
        # lambda to convert a number to alphabet
        # 1 -> a, 2 -> b, 3 -> c, etc.
        x = lambda x: chr(x + 96)
        await ctx.response.send_message(f"Answer: **{x(choice)}**")
    
def setup(bot): 
    bot.add_cog(Flip(bot)) 
