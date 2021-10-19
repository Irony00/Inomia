import discord
from discord.ext import commands

class Colours(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["green"])
    async def _green(self, ctx):
        embed = discord.Embed(
            title = "Green",
            color = discord.Color.green()
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/cc/18/a5/cc18a5901d40c79d27a3c38584329956.gif"
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["blue"])
    async def _blue(self, ctx):
        embed = discord.Embed(
            title = "Blue",
            color = discord.Color.dark_blue()
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/d0/e2/a8/d0e2a8ae4195b8105ceb7477267367e1.gif"
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["light"])
    async def _light(self, ctx):
        embed = discord.Embed(
            title = "Light",
            color = 0xFFFFFF
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/64/ce/9f/64ce9f3c2463b528dfba90720fed9ea5.gif"
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["purplepink"])
    async def _purplepink(self, ctx):
        embed = discord.Embed(
            title = "Purple - Pink",
            color = discord.Color.purple()
        )
        embed.set_image(
            url = "https://cutewallpaper.org/21/anime-fantasy-scenery/gif-sky-moon-space-purple-clouds-Magic-fantasy-scenery-.gif"
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["red"])
    async def _red(self, ctx):
        embed = discord.Embed(
            title = "Red",
            color = discord.Color.red()
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/9b/da/90/9bda90c406615bfb08c1deee5eac12f0.gif"
        )
        await ctx.send(embed = embed)

    @commands.command(aliases = ["orange"])
    async def _orange(self, ctx):
        embed = discord.Embed(
            title = "Orange",
            color = discord.Color.red()
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/a6/eb/2f/a6eb2f38b2323718b0e318ed2b59f57e.gif"
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["orange"])
    async def _orange(self, ctx):
        embed = discord.Embed(
            title = "Orange",
            color = discord.Color.red()
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/a6/eb/2f/a6eb2f38b2323718b0e318ed2b59f57e.gif"
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["cyan"])
    async def _cyan(self, ctx):
        embed = discord.Embed(
            title = "Cyan",
            color = discord.Color.blue()
        )
        embed.set_image(
            url = "https://images.unsplash.com/photo-1568607689150-17e625c1586e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXwzNTE3MjB8fGVufDB8fHx8&w=1000&q=80"
        )
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Colours(bot))