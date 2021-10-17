import random
import asyncio
import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def welcome_embed(self, new_member):
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
            f"Help us, **<@{ new_member.id }>**. You are our only hope.",
            f"**<@{ new_member.id }>**, did you bring the pizza, or was that someone else.",
            f"It is perilous to study too deeply the arts of **<@{ new_member.id }>**, for good or for ill.",
            f"Initializing welcome system for **<@{ new_member.id }>**...",
            f"**<@{ new_member.id }>**, you can't fight in here! This is the War Room!",
            f"Arise, arise Angels of Insomnia! Fell deeds awake: bugs and crashes! Mice shall be shaken, keyboards be splintered, a sleep day, a red day, ere the sun rises! Ride now, ride now! Ride to Hunter Reilly! Welcome **<@{ new_member.id }>**."
        ]

        # Embed
        embed = discord.Embed(
            title = "Welcome",
            description = random.choice(descriptions),
            color = random.choice(colors)
        )
        embed.set_thumbnail(
            url = new_member.avatar_url
        )

        return embed

    @commands.Cog.listener()
    async def on_member_join(self, new_member):
        # wait_time = 60
        general_id = discord.utils.get(self.bot.get_all_channels(), name = "😃┃general-chat")
        general_channel = self.bot.get_channel(general_id.id)
        embed = self.welcome_embed(new_member)
        message = await general_channel.send(embed = embed)
        await message.add_reaction("👋")
        # await asyncio.sleep(wait_time)
        # await message.delete()
    
    @commands.command(aliases = ["welcome", "wlcm"])
    async def _welcome_me(self, ctx):
        # wait_time = 60
        author = ctx.message.author
        embed = self.welcome_embed(author)
        message = await ctx.send(embed = embed)
        await message.add_reaction("👋")
        # await asyncio.sleep(wait_time)
        # await message.delete()

def setup(bot):
    bot.add_cog(Greetings(bot))