import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def make_loader(self, progress, total):
        loader_length = 30
        progress_unit = "█"
        progress_length = int(( progress / total ) * loader_length) + 1
        space_length = loader_length - progress_length

        inner_loader = ""
        for i in range(0, progress_length):
            inner_loader += progress_unit
        
        for i in range(0, loader_length - progress_length):
            inner_loader += " "
        
        embed = discord.Embed(
            description = f"Progress ... \n```[{inner_loader}]```"
        )

        return embed
        

    @commands.command(aliases = ["nickname_suffix", "ns"])
    async def _add_nickname_suffix(self, ctx, *, suffix):
        if not ctx.message.author.guild_permissions.administrator:
            await ctx.channel.send("You don't have permission to use this command.")
            return

        log = await ctx.channel.send("Revising all nicknames ...")

        progress = 0
        members_list = ctx.message.guild.members
        for member in ctx.message.guild.members:
            display_name = member.display_name
            new_name = suffix + " " + display_name

            try:
                await member.edit(nick = new_name)
            except discord.errors.Forbidden:
                continue
            except discord.errors.HTTPException:
                continue
            finally:
                total = len(members_list)
                print(progress)
                loader = self.make_loader(progress, total)
                await log.edit(embed = loader)
                progress += 1
        
        await log.edit(content = "All nicknames has been revised.")

    @commands.command(aliases = ["reset_nicknames", "rn"])
    async def _reset_nickname(self, ctx):
        if not ctx.message.author.guild_permissions.administrator:
            await ctx.channel.send("You don't have permission to use this command.")
            return

        log = await ctx.channel.send("Resetting all nicknames ...")

        progress = 0
        members_list = ctx.message.guild.members
        for member in members_list:
            try:
                await member.edit(nick = member.name)
            except discord.errors.Forbidden:
                continue
            finally:
                total = len(members_list)
                loader = self.make_loader(progress, total)
                await log.edit(embed = loader)
                progress += 1
        
        await log.edit(content = "All nicknames has been reset.")

def setup(bot):
    bot.add_cog(Events(bot))