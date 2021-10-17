import os
import random
import discord
import asyncio
import requests
import bs4 as bs
from dotenv import load_dotenv
from discord.ext import commands
from requests.models import Response
load_dotenv()

intents = discord.Intents.default()
intents.members = True

token = os.getenv("TOKEN")
bot = commands.Bot(
    command_prefix = ".",
    intents=intents
)

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_join(member):
    wait_time = 60

    general_id = discord.utils.get(bot.get_all_channels(), name = "😃┃general-chat")
    general_channel = bot.get_channel(general_id.id)

    colors = [
        discord.Color.red(),
        discord.Color.blue(),
        discord.Color.green(),
        discord.Color.purple(),
        discord.Color.orange(),
        discord.Color.dark_red(),
        discord.Color.dark_blue(),
        discord.Color.dark_green(),
        discord.Color.dark_purple(),
        discord.Color.dark_orange()
    ]

    descriptions = [
        f"Help us, **<@{ member.id }>**. You are our only hope.",
        f"**<@{ member.id }>**, did you bring the pizza, or was that someone else.",
        f"It is perilous to study too deeply the arts of **<@{ member.id }>**, for good or for ill.",
        f"Initializing welcome system for **<@{ member.id }>**...",
        f"**<@{ member.id }>**, you can't fight in here! This is the War Room!",
        f"Arise, arise Angels of Insomnia! Fell deeds awake: bugs and crashes! Mice shall be shaken, keyboards be splintered, a sleep day, a red day, ere the sun rises! Ride now, ride now! Ride to Hunter Reilly! Welcome **<@{ member.id }>**."
    ]

    embed = discord.Embed(
        title = "Welcome",
        description = random.choice(descriptions),
        color = random.choice(colors)
    )
    embed.set_thumbnail(
        url = member.avatar_url
    )

    message = await general_channel.send(embed = embed)
    await message.add_reaction("👋")
    await asyncio.sleep(wait_time)
    await message.delete()
    
@bot.command(aliases = ["talk"])
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

@bot.command(aliases = ["welcome", "wlcm"])
async def _welcome_me(ctx):
    author = ctx.message.author
    wait_time = 60

    colors = [
        discord.Color.red(),
        discord.Color.blue(),
        discord.Color.green(),
        discord.Color.purple(),
        discord.Color.orange(),
        discord.Color.dark_red(),
        discord.Color.dark_blue(),
        discord.Color.dark_green(),
        discord.Color.dark_purple(),
        discord.Color.dark_orange()
    ]

    descriptions = [
        f"Help us, **<@{ author.id }>**. You are our only hope.",
        f"**<@{ author.id }>**, did you bring the pizza, or was that someone else.",
        f"It is perilous to study too deeply the arts of **<@{ author.id }>**, for good or for ill.",
        f"Initializing welcome system for **<@{ author.id }>**...",
        f"**<@{ author.id }>**, you can't fight in here! This is the War Room!",
        f"01010111 01100101 01101100 01100011 01101111 01101101 01100101 **<@{ author.id }>**",
        f"Arise, arise Angels of Insomnia! Fell deeds awake: bugs and crashes! Mice shall be shaken, keyboards be splintered, a sleep day, a red day, ere the sun rises! Ride now, ride now! Ride to Hunter Reilly! Welcome **<@{ author.id }>**."
    ]

    embed = discord.Embed(
        title = "Welcome",
        description = random.choice(descriptions),
        color = random.choice(colors)
    )
    embed.set_thumbnail(
        url = author.avatar_url
    )

    message = await ctx.send(embed = embed)
    await message.add_reaction("👋")
    await asyncio.sleep(wait_time)
    await message.delete()

bot.run(token)