import discord
from discord.ext import commands
"""_summary_
refer to https://guide.pycord.dev/popular-topics/cogs for more info
"""
class Greetings(commands.Cog): 

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @commands.command()
    async def hello(self, ctx): 
        await ctx.send('Hello!')

    @discord.slash_command() # we can also add application commands
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye!')

    @discord.user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')

    @commands.Cog.listener() # we can add event listeners to our cog
    async def on_member_join(self, member): # this is called when a member joins the server
    # you must enable the proper intents
    # to access this event.
    # See the Popular-Topics/Intents page for more info
        await member.send('Welcome to the server!')

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Greetings(bot)) # add the cog to the bot