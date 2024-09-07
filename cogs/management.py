import discord
from discord.ext import commands


class ManagementCog(commands.Cog):
    
        def __init__(self, bot):
            self.bot = bot  # adding a bot attribute for easier access
    
        # adding a command to the cog
        @commands.command(name="info")
        async def slash_cmdinfo(self, ctx: discord.Interaction):
            embed = discord.Embed(color=discord.Color.brand_green(), title=ctx.guild.name)
            embed.add_field(name="Members", value=len([member for member in ctx.guild.members if not member.bot]), inline=True)
            embed.add_field(name="Bots", value=len([member for member in ctx.guild.members if member.bot]), inline=True)
            embed.set_thumbnail(url=ctx.guild.icon)
            embed.set_footer(text="Created at " + ctx.guild.created_at.strftime("%d-%m-%Y"), icon_url=ctx.guild.icon)
            await ctx.response.send_message(embed=embed)
        
        @commands.command(name="about")
        async def slash_cmdabout(self, ctx: discord.Interaction, member: discord.Member):
            if member.avatar is None:
                avatar = member.default_avatar
            else:
                avatar = member.avatar
            var = {1: "st", 2: "nd", 3: "rd", 4: "th"}
            color = member.top_role.color if member.top_role.color != discord.Color.default() else discord.Color.brand_green()
            embed = discord.Embed(title=member.global_name or member.name, color=color)
            members_sorted = sorted(ctx.guild.members, key=lambda member: member.joined_at)
            member_index = members_sorted.index(member) + 1
            embed.description = f"**Name: **{member.name}\n **ID: **{member.id}\n **Status: **{str(member.status).title()}\n **Top Role: **`{member.top_role}`\n **Joined at: **{member.joined_at.strftime('%d-%m-%Y')} [{member_index }{var[member_index] if member_index < 4 else  var[4]}]"
            embed.set_thumbnail(url=avatar) 
            embed.set_footer(text="Created at " + member.created_at.strftime("%d-%m-%Y"), icon_url=avatar)
            await ctx.response.send_message(embed=embed)

async def setup(bot):
    # finally, adding the cog to the bot
    await bot.add_cog(ManagementCog(bot=bot))
