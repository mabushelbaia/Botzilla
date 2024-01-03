import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    intents=discord.Intents.all(),
)
GUILD, BOT_ROLE, MEMBER_ROLE, MEMBER_COUNT_CHANNEL, BOT_COUNT_CHANNEL, WELCOME_CHANNEL = None, None, None, None, None, None


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
    global GUILD, BOT_ROLE, MEMBER_ROLE, MEMBER_COUNT_CHANNEL, BOT_COUNT_CHANNEL, WELCOME_CHANNEL
    GUILD = bot.get_guild(464129710797094912)
    BOT_ROLE = GUILD.get_role(1191535463241105458)
    MEMBER_ROLE = GUILD.get_role(930490861408645151)
    MEMBER_COUNT_CHANNEL = bot.get_channel(1192083973493510164)
    BOT_COUNT_CHANNEL = bot.get_channel(1192084004233556019)
    WELCOME_CHANNEL = bot.get_channel(750030117866176662)
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

    embed = discord.Embed(
        title=f"Welcome to {GUILD.name}!",
        color=discord.brand_green(),
        timestamp=member.joined_at,
    )
    embed.set_thumbnail(url=member.avatar)
    embed.set_author(name=GUILD.name, icon_url=GUILD.icon, url="https://discord.gg/mAea8Ekqq9")
    members_sorted = sorted(GUILD.members, key=lambda member: member.joined_at)
    member_index = members_sorted.index(member) + 1
    var = {1: "st", 2: "nd", 3: "rd"}
    if member_index < 4:
        embed.description = f"**{member.global_name}** is the **{member_index}{var[member_index]}** member of {GUILD.name}!"
    else:
        embed.description = f"**{member.global_name}** is the **{member_index}th** member of {GUILD.name}! "

    await WELCOME_CHANNEL.send(embed=embed)


@bot.command()
async def test(ctx: commands.Context):
    embed = discord.Embed(
        title=f"Welcome to {GUILD.name}!",
        color=discord.Color.random(),
        timestamp=ctx.author.joined_at,
    )
    embed.set_thumbnail(url=ctx.author.avatar)
    embed.set_author(name=GUILD.name, icon_url=GUILD.icon,
                     url="https://discord.gg/mAea8Ekqq9")
    members_sorted = sorted(GUILD.members, key=lambda member: member.joined_at)
    member_index = members_sorted.index(ctx.author) + 1
    var = {1: "st", 2: "nd", 3: "rd"}
    if member_index < 4:
        embed.description = f"**{ctx.author.global_name}** is the **{member_index}{var[member_index]}** member of {GUILD.name}!"
    else:
        embed.description = f"**{ctx.author.global_name}** is the **{member_index}th** member of {GUILD.name}! "
    await ctx.send(embed=embed)

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
