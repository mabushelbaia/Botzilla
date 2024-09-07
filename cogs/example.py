from discord import app_commands
from discord.ext import commands


# all cogs inherit from this base class
class ExampleCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot  # adding a bot attribute for easier access
        self.member_count = 0
        self.bot_count = 0

    # adding a slash command to the cog (make sure to sync this!)
    @app_commands.command(name="ping")
    async def slash_pingcmd(self, interaction):
        """the second best command in existence"""
        await interaction.response.send_message(interaction.user.mention)

    @app_commands.command(name="clear")
    async def slash_clearcmd(self, interaction, amount: int):
        """clears messages"""
        if not interaction.channel.permissions_for(
                interaction.user).manage_messages:
            return await interaction.response.send_message(
                "You don't have the required permissions to use this command!",
                ephemeral=True)
        if amount < 1:
            return await interaction.response.send_message(
                "You need to specify an amount of messages to clear!",
                ephemeral=True)
        if amount > 100:
            return await interaction.response.send_message(
                "You can only clear up to 100 messages at once!",
                ephemeral=True)
        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(
            f"Clearing {amount} messages...")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot is ready! Logged in as {self.bot.user}")
        self.member_count = self.bot.guilds[0].member_count
        self.bot_count = len([member for member in self.bot.guilds[0].members if member.bot])
        await self.bot.get_channel(1192083973493510164).edit(name=f"🥷︱Members - {self.member_count - self.bot_count}")
        await self.bot.get_channel(1192084004233556019).edit(name=f"🤖︱Bots - {self.bot_count}")

        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(f"Error syncing commands: {e}")
    @commands.Cog.listener()
    async def on_member_join(self, member):
        self.member_count += 1
        if member.bot:
            self.bot_count += 1
        await self.bot.get_channel(1192083973493510164).edit(name=f"🥷︱Members - {self.member_count - self.bot_count}")
        await self.bot.get_channel(1192084004233556019).edit(name=f"🤖︱Bots - {self.bot_count}")
        welcome_channel = self.bot.get_channel(750030117866176662)

        await welcome_channel.send(f"Welcome to the server, {member.mention}! Make sure to read the rules and have fun!")
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        self.member_count -= 1
        if member.bot:
            self.bot_count -= 1
        await self.bot.get_channel(1192083973493510164).edit(name=f"🥷︱Members - {self.member_count - self.bot_count}")
        await self.bot.get_channel(1192084004233556019).edit(name=f"🤖︱Bots - {self.bot_count}")
        welcome_channel = self.bot.get_channel(750030117866176662)

        await welcome_channel.send(f"{member.mention} has left the server. Goodbye!")
# usually you’d use cogs in extensions
# you would then define a global async function named 'setup', and it would take 'bot' as its only parameter
async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(ExampleCog(bot=bot))
