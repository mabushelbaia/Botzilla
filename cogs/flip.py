import random
import time
import discord
from discord.ext import commands

random.seed(time.time())


class Flip(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Flips a coin given a prompt")
    async def flip(self, ctx, prompt: str, heads: str, tails: str) -> None:
        choice = "Heads" if random.randint(0, 1) == 1 else "Tails"

        embed = discord.Embed(title=prompt, color=discord.Color.yellow())
        embed.add_field(name="**Heads**", value=heads.title())
        embed.add_field(name="**Tails**", value=tails.title())
        embed.description = (
            f'**{choice}:** {heads.title() if choice == "Heads" else tails.title()}'
        )
        heads_file = discord.File("img/heads.png", filename="heads.png")
        tails_file = discord.File("img/tails.png", filename="tails.png")
        if choice == "Heads":
            embed.set_thumbnail(url="attachment://" + heads_file.filename)
        else:
            embed.set_thumbnail(url="attachment://" + tails_file.filename)
        embed.set_footer(
            text=f"Flipped by {ctx.user.name}", icon_url=ctx.user.avatar)
        file = heads_file if choice == "Heads" else tails_file
        await ctx.response.send_message(embed=embed, file=file)

    @discord.slash_command(description="Flips a coin without a prompt")
    async def coin(self, ctx) -> None:
        choice = "Heads" if random.randint(0, 1) == 1 else "Tails"
        await ctx.response.send_message(f"**{choice}**")

    @discord.slash_command(description="Rolls a dice")
    async def roll(self, ctx) -> None:
        choice = random.randint(1, 6)
        await ctx.response.send_message(f"You rolled a **{choice}**")


def setup(bot): 
    bot.add_cog(Flip(bot)) 
