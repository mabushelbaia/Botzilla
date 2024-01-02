import discord
from discord.ext import commands



class Management(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="Kick a user")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if (ctx.author.guild_permissions.kick_members):
            await member.kick(reason=reason)
            await ctx.response.send_message(f"Kicked {member.mention}")
        else:
            await ctx.response.send_message("You don't have the permission to do that")
    
    @discord.slash_command(description="Ban a User")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if (ctx.author.guild_permissions.ban_members):
            try:
                await member.ban(reason=reason)
                await ctx.response.send_message(f"Banned {member.mention}")
            except:
                await ctx.response.send_message("Something went wrong you might not have the permission to do that")
        else:
            await ctx.response.send_message("You don't have the permission to do that")
    
    @discord.slash_command(description="Clear messages")
    async def clear(self, ctx, amount=5):
        if (ctx.author.guild_permissions.manage_messages):
            try:
                await ctx.channel.purge(limit=int(amount))
                await ctx.response.send_message(f"Cleared {amount} messages")
            except:
                await ctx.response.send_message("Something went wrong you might not have the permission to do that")
        else:
            await ctx.response.send_message("You don't have the permission to do that")
    
    @discord.slash_command(description="Disconnect an user")
    async def disconnect(self, ctx, member: discord.Member, *, reason=None):
        if (ctx.author.guild_permissions.move_members):
            await member.move_to(None, reason=reason)
            await ctx.response.send_message(f"Disconnected {member.mention}")
        else:
            await ctx.response.send_message("You don't have the permission to do that")
    
    @discord.slash_command(description="Get user info")
    async def about(self, ctx, member: discord.Member):
        if member.avatar is None:
            avatar = member.default_avatar
        else:
            avatar = member.avatar
        embed = discord.Embed(title=member.name + "'s Information", color=discord.Color.blue())
        embed.add_field(name="Name", value=member.name, inline=False)
        embed.add_field(name="Top Role", value=member.top_role.name, inline=False)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%d-%m-%Y"), inline=False)
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text="Joined at " + member.joined_at.strftime("%d-%m-%Y"), icon_url=avatar)
        await ctx.response.send_message(embed=embed)
    
    @discord.slash_command(description="Get server info")
    async def server(self, ctx: discord.Interaction):
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Members", value=len([member for member in ctx.guild.members if not member.bot]), inline=True)
        embed.add_field(name="Bots", value=len([member for member in ctx.guild.members if member.bot]), inline=True)
        embed.set_thumbnail(url=ctx.guild.icon)
        embed.set_author(name=ctx.guild.name, url="https://discord.gg/mAea8Ekqq9")
        embed.set_footer(text="Created at " + ctx.guild.created_at.strftime("%d-%m-%Y"), icon_url=ctx.guild.icon)
        await ctx.response.send_message(embed=embed)
    
    @discord.slash_command(description="Get latency")
    async def ping(self, ctx):
        await ctx.response.send_message(f"Pong! {round(self.bot.latency * 1000)}ms")
    

def setup(bot):  
    bot.add_cog(Management(bot)) 
