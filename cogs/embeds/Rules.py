import discord
from discord.ext import commands

rules = '''
Please keep the following rules in mind when talking.

‣ Be respectful
‣ No spamming 
‣ No swearing
‣ Any form of racism, gore, etc are forbidden
‣ Don't advertise without permission from staffs
‣ Talks about religion and politics can be taken to DMs
‣ Maintain our server standards

By staying in the community you agree with the given rules
'''

class Rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["rules", "rule"])
    async def _rule(self, ctx):
        embed = discord.Embed(
            title = "Rules",
            description = rules,
            color = discord.Color.blue()
        )
        embed.set_footer(
            text = "Team Insomnia",
            icon_url = "https://media.discordapp.net/attachments/898127603922239513/898816884621848616/yerOW6.jpg?width=524&height=393"
        )
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["rules_image", "rule_image", "rule_img"])
    async def _rule_image(self, ctx):
        embed = discord.Embed()
        embed.set_image(url = "https://media.discordapp.net/attachments/898436139164266507/898900778973032478/RULES.png")
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Rules(bot))