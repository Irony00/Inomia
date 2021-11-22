import asyncio
import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.snipe = {
            "content": None,
            "author": None,
            "author_pfp": None,
            "message_id": None
        }

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.snipe["content"] = message.content
        self.snipe["author"] = message.author
        self.snipe["author_pfp"] = message.author.avatar_url
        self.snipe["message_id"] = message.id
        await asyncio.sleep(60)

        if message.id == self.snipe["message_id"]:
            self.snipe["content"] = None
            self.snipe["author"] = None
            self.snipe["author_pfp"] = None
            self.snipe["message_id"] = None

    @commands.command(aliases = ["snipe", "s"])
    async def _snipe(self, ctx):
        if self.snipe["message_id"] == None:
            await ctx.send("I saw nothing @_@")
            return

        em = discord.Embed(
            title = "Caught ya!", 
            description = self.snipe["content"],
            color = discord.Color.purple()
        )
        em.set_footer(text = self.snipe["author"])
        em.set_thumbnail(url = self.snipe["author_pfp"])

        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Fun(bot))
