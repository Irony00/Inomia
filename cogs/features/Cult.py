import discord
import asyncio
import discord.utlis
from discord.ext import commands
from discord.utils import get

class Cult(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
          
    @commands.command()
    @has_permissions(administrator=True)
    async def addrole(ctx, role: discord.Role, user: discord.Member):
        await user.add_roles(role)
        await ctx.send(f"Assigned [role.mention] to [user.mention]")

def setup(bot):
    bot.add_cog(Cult(bot))
