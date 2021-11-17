import discord
from discord.ext import commands

class Support(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      
    @commands.command(aliases = ["feedback", "fb"])
    async def _feedback(self, ctx, *args):
        feedback = " ".join(args)
        user = ctx.message.author
        await ctx.send('Your feedback has been sent!')
        channel = self.bot.get_channel(910367070397534228)
        msg = await channel.send(f'**New Feedback by {user}:** {feedback}')
        await msg.add_reaction('✅')
        await msg.add_reaction('⛔')
        await ctx.message.delete()
        
def setup(bot):
    bot.add_cog(Support(bot))
