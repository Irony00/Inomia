import discord
from discord.ext import commands

class SnipeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.snipe = {}

    @commands.Cog.listener()
    async def on_message_delete(message):
        self.snipe[message.channel.id]["author"] = message.author             
        self.snipe[message.channel.id]["content"] = message.content
        await sleep (60)
        del snipe_message[message.channel.id]

    @commands.command()
    async def snipe(ctx):
        channel = ctx.channel
        content = self.snipe[channel.id]["content"]
        author = self.snipe[channel.id]["author"]
        try: 
            em = discord.Embed(name = f"gottem #{channel.name}", description = content)
            em.set_footer(text = f"this man {author}")
            await ctx.send(embed = em)
        except: 
            await ctx.send(f"There are no recent deleted messages in #{channel.name}")

def setup(bot):
    bot.add_cog(SnipeCog(bot))
