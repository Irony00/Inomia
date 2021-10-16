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

@bot.command(aliases = ["rules", "rule"])
async def _rule(ctx):
    embed = discord.Embed(
        title = "Rules",
        description = '''
            Please keep the following rules in mind when talking.

            ‣ Be respectful
            ‣ No spamming 
            ‣ Any form of racism, gore, etc are forbidden
            ‣ Don't advertise without permission from staffs
            ‣ Talks about religion and politics can be taken to DMs
            ‣ Maintain our server standards

            By staying in the community you agree with the given rules
        ''',
        color = discord.Color.blue()
    )
    embed.set_footer(
        text = "Team Insomnia",
        icon_url = "https://media.discordapp.net/attachments/898127603922239513/898816884621848616/yerOW6.jpg?width=524&height=393"
    )

    await ctx.send(embed = embed)

@bot.command(aliases = ["rules_image", "rule_image", "rule_img"])
async def _rule_image(ctx):
    embed = discord.Embed()
    embed.set_image(url = "https://media.discordapp.net/attachments/898436139164266507/898900778973032478/RULES.png")

    await ctx.send(embed = embed)

bot.run(token)