import discord
from discord.ext import commands
import random

easter = ["Keep the rules in mind and enjoy your time here ^-^","You can give your feedback abt the bot using the feedback command","You can get support here:- https://discord.gg/UYBKcTYzyU"]

class SugsCog(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        adPer = random.randrange(0, 30)
        if adPer < 2:
            await ctx.send(random.choice(easter))

def setup(bot):
    bot.add_cog(SugsCog(bot))
