import discord
import asyncio
from discord.ext import commands
from discord.utils import get

class Cult(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
          
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addrole(ctx, role: discord.Role, user: discord.User):
        guild = ctx.guild
        mem = guild.get_member(user.id)
        await mem.add_roles(role)
        await ctx.send(f"Assigned {role.mention} to {mem.mention}")

def setup(bot):
    bot.add_cog(Cult(bot))
