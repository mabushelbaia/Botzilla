import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=discord.Intents.all(),
)
GUILD, BOT_ROLE, MEMBER_ROLE, MEMBER_COUNT_CHANNEL, BOT_COUNT_CHANNEL = None, None, None, None, None

async def update_member_count():
    MEMBER_COUNT = len([member for member in GUILD.members if not member.bot])
    BOT_COUNT = len([member for member in GUILD.members if member.bot])
    await MEMBER_COUNT_CHANNEL.edit(name=f"🥷︱Members - {MEMBER_COUNT}", pinned=True)
    await BOT_COUNT_CHANNEL.edit(name=f"🤖︱Bots - {BOT_COUNT}")
async def update_members():
    for member in GUILD.members:
        if (BOT_ROLE in member.roles) or (MEMBER_ROLE in member.roles):
            continue
        if member.bot:
            await member.add_roles(BOT_ROLE)
        else:
            await member.add_roles(MEMBER_ROLE)


@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)
    global GUILD, BOT_ROLE, MEMBER_ROLE, MEMBER_COUNT_CHANNEL, BOT_COUNT_CHANNEL
    GUILD = bot.get_guild(464129710797094912)
    BOT_ROLE = GUILD.get_role(1191535463241105458)
    MEMBER_ROLE = GUILD.get_role(930490861408645151)
    MEMBER_COUNT_CHANNEL = bot.get_channel(1192083973493510164)
    BOT_COUNT_CHANNEL = bot.get_channel(1192084004233556019)
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="You!"))
    await update_members()
    await update_member_count()

@bot.event
async def on_member_join(member):
    if member.bot:
        await member.add_roles(BOT_ROLE)
    else:
        await member.add_roles(MEMBER_ROLE)
    await update_member_count()

@bot.event
async def on_member_remove(member):
    await update_member_count()

cog_list = ["split", "flip", "management"]
for cog in cog_list:
    bot.load_extension(f"cogs.{cog}")

if __name__ == "__main__":
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    bot.run(BOT_TOKEN)
