import os
import discord
import requests
import bs4 as bs
from dotenv import load_dotenv
from discord.ext import commands
from requests.models import Response
load_dotenv()

token = os.getenv("TOKEN")
bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.command(aliases = ["talk"])
async def _talk(ctx, *, question, user: discord.Member = None):
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

bot.run(token)