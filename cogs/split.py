from attr import dataclass
import discord
import random
import time
from discord.ext import commands
random.seed(time.time())


@dataclass
class Team:
    name: str
    members: list[discord.Member]


class Split(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Splits a voice channel into two teams")
    async def split_channel(self, ctx, channel: discord.VoiceChannel, team1: str, team2: str) -> None:
        members = channel.members
        random.shuffle(members)
        team_1 = Team(team1, members[: len(members) // 2])
        team_2 = Team(team2, members[len(members) // 2:])

        team1_string = "\n".join(
            [":small_blue_diamond:  `" + member.name +
                "`" for member in team_1.members]
        )
        team2_string = "\n".join(
            [":small_orange_diamond:   `" + member.name +
                "`" for member in team_2.members]
        )
        embed = discord.Embed(title="**Splitted Teams**",
                              color=discord.Color.yellow())
        embed.add_field(name=f"**Team {team_1.name}**", value=team1_string)
        embed.add_field(name=f"**Team {team_2.name}**", value=team2_string)
        embed.set_footer(
            text=f"Requested by {ctx.user}", icon_url=ctx.user.avatar)
        await ctx.response.send_message(embed=embed, view=MyView(team_1, team_2))

class MyView(discord.ui.View):
    def __init__(self, team_1, team_2):
        super().__init__()
        self.team1 = team_1
        self.team2 = team_2
        self.team1_members = [member for member in team_1.members]
        self.team2_members = [member for member in team_2.members]

    @discord.ui.button(label="Split", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction: discord.Interaction):
        button.disabled = True
        voice_channel_1 = interaction.guild.get_channel(1191113463272058880)
        voice_channel_2 = interaction.guild.get_channel(1191113512722907267)

        await voice_channel_1.edit(
            name="Team " + self.team1.name, user_limit=len(self.team1.members)
        )
        await voice_channel_2.edit(
            name="Team " + self.team2.name, user_limit=len(self.team2.members)
        )

        for member in self.team1_members:
            await member.move_to(voice_channel_1)
        for member in self.team2_members:
            await member.move_to(voice_channel_2)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="Shuffle", row=0, style=discord.ButtonStyle.danger)
    async def second_button_callback(self, button, interaction):
        members = self.team1_members + self.team2_members
        random.shuffle(members)
        self.team1_members = members[: len(members) // 2]
        self.team2_members = members[len(members) // 2:]
        embed = discord.Embed(title="**Splitted Teams**",
                              color=discord.Color.yellow())
        team1_string = "\n".join(
            [":small_blue_diamond: ` - " + member.name +
                "`" for member in self.team1_members]
        )
        team2_string = "\n".join(
            [":small_orange_diamond:   ` - " + member.name +
                "`" for member in self.team2_members]
        )
        embed.add_field(name=f"**Team {self.team1.name}**", value=team1_string)
        embed.add_field(name=f"**Team {self.team2.name}**", value=team2_string)
        embed.set_footer(
            text=f"Requested by {interaction.user}", icon_url=interaction.user.avatar)
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="Cancel", row=0, style=discord.ButtonStyle.secondary)
    async def third_button_callback(self, button, interaction):
        await interaction.response.edit_message(view=None)


def setup(bot):
    bot.add_cog(Split(bot))
