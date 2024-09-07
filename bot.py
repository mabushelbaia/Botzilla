import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


class ExampleBot(commands.Bot):
    def __init__(self):
        # initialize our bot instance, make sure to pass your intents!
        # for this example, we'll just have everything enabled
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    # the method to override in order to run whatever you need before your bot starts
    async def setup_hook(self):
        for filename in os.listdir("cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")


ExampleBot().run(TOKEN)
