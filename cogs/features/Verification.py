import discord
from discord.ext import commands

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        verify_me_channel_id = 900721804388237372
        content = message.content
        channel_id = message.channel.id
        author = message.author
        author_name = author.name
        verify_role = discord.utils.get(author.guild.roles, name = "Verified Hooter")

        i_hoot_variation = [".iHoot", ".i_hoot", ".ihoot"]

        if channel_id == verify_me_channel_id:
            if content in i_hoot_variation:
                await author.add_roles(verify_role)
                await author.send(f"Thank you **{ author_name }**, for verifying yourself. Welcome to **Insomnia**!")
                await message.delete()
            else:
                await message.delete()

def setup(bot):
    bot.add_cog(Verification(bot))