import discord
from discord.ext import commands

class Counter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        counter_channel_id = 900640249661780028
        counter_channel = None
        
        if not message.content.isnumeric():
            return

        for channel in message.guild.channels:
            if channel.id == counter_channel_id:
                counter_channel = channel
        
        if counter_channel== None:
            return

        messages = await counter_channel.history(limit = 2).flatten()      
        last_message = messages[1]
        if int(message.content) == int(last_message.content) + 1:
            await message.channel.edit(name = f"{message.content}┃counting")
            

def setup(bot):
    bot.add_cog(Counter(bot))