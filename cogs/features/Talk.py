import requests
import discord
import bs4 as bs
from discord.ext import commands

class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["talk"])
    async def _talk(ctx, *, question, user: discord.Member = None):
        async with ctx.typing():
            url = 'https://www.pandorabots.com/pandora/talk?botid=cd44746d1e3755a1'
            question_filtered = question.replace("insomnia", "spacegy4")
            user = ctx.author
            query = {
                'input': question_filtered, 
                "botcust2": user
            }
            response = requests.post(url, data = query)
            soup = bs.BeautifulSoup(response.text, 'lxml')
            
            answer = soup.find_all("font")[2].text
            answer_filtered = answer.replace("spacegy4", "insomnia")
            await ctx.send(answer_filtered)
    

def setup(bot):
    bot.add_cog(Talk(bot))