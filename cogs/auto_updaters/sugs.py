import discord
from discord.ext import commands
import random

outside_server_easters = ["You can get support here:- https://discord.gg/UYBKcTYzyU"]
easter = ["The credit for the spicy hot waifu and husbando pics go to Tanjiro#3129, yami#2835, SALMON#8537. True legends :pray: ","Keep the rules in mind and enjoy your time here ^-^","You can give your feedback abt the bot using the feedback command"]

class SugsCog(commands.Cog):
    def __init__(self, bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
      adPer = random.randrange(0, 30)
      if adPer < 2:
        easter_choice = random.choice(easter + outside_server_easters)
        
        insomnia_server_id = "898127603309899806"
        if ctx.guild.id == insomnia_server_id and easter_choice in outside_server_easters:
            return

        await ctx.send(random.choice(easter))

def setup(bot):
    bot.add_cog(SugsCog(bot))
