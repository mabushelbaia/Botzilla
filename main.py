import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=discord.Intents.all(),
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")



@bot.event
async def on_ready():
    print("Logged in as" + bot.user.name + " (ID:" + str(bot.user.id) )
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="You!"))


cog_list = ["split", "flip"]
for cog in cog_list:
    bot.load_extension(f"cogs.{cog}")

bot.run(BOT_TOKEN)
