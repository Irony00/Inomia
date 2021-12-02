import discord
from discord.ext import commands

class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emdict = {}
    
    @commands.command()
    async def embed(self,ctx):
        await ctx.send("Enter title for embed (Enter skip or none to skip)")
        title = await self.bot.wait_for('message',check = lambda message: message.author == ctx.author,timeout=30)
        if title.content == "none" or title.content == "skip":
            title.content = " "
        await ctx.send("Enter the url for image to be attached (skip/none if not applicable)")
        image = await self.bot.wait_for('message',check = lambda message: message.author == ctx.author,timeout=30)
        if image.content == "none" or image.content == "skip":
            image.content = " "
        await ctx.send("Enter the number of fields(an integer from 0-10) you want in your embed (skip/none to skip)")
        fnum = await self.bot.wait_for('message',check = lambda message: message.author == ctx.author,timeout=30)
        if fnum.content == "none" or fnum.content == "skip":
            fnum.content = " "
        for i in range(int(fnum.content)):
            await ctx.send("Enter name of field")
            field = await self.bot.wait_for('message',check = lambda message: message.author == ctx.author,timeout=30)
            await ctx.send("Enter value of field")
            fieldval = await self.bot.wait_for('message',check = lambda message: message.author == ctx.author,timeout=30)
            dict = self.emdict
            dict[ctx.author.id][field.content] = fieldval.content
        em = discord.Embed(title=title)
        if image.content != " ":
            em.set_image(image)
        for i in self.dict[ctx.author.id]:
            em.add_field(name=i,value=self.dict[ctx.author.id][i])
        await ctx.send("Enter channelid of the channel where u want to send the embed")
        channel = await self.bot.wait_for('message',check = lambda message: message.author == ctx.author,timeout=30)
        ch = self.bot.fetch_channel(channel.content)
        await ch.send(embed=em)
        
        
def setup(bot):
    bot.add_cog(EmbedCog(bot))
