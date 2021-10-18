import random
import asyncio
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["warn"])
    async def _warn(self, ctx, user : discord.User, *, reason = None):
        reason = "Dumbass forgot to put a reason" if reason == None else reason

        # Creating Embed
        embed = discord.Embed(
            description = f"**Reason:** { reason }"
        )
        embed.set_author(
            name = f"{ user } has been warned",
            url = user.avatar_url
        )

        await ctx.send(f"<@{ user.id }>", embed = embed)
    
    @commands.command(aliases = ["kick"])
    async def _kick(self, ctx, user : discord.User, *, reason = None):
        reason = "Dumbass forgot to put a reason" if reason == None else reason

        kick_gif_list = [
            "https://c.tenor.com/Gf6UTsRayw4AAAAC/kickers-caught.gif",
            "https://c.tenor.com/WXJF2QatHA4AAAAC/anime-ouch.gif",
            "https://c.tenor.com/TY_AmszVhJIAAAAC/oh-yeah-high-kick.gif",
            "https://c.tenor.com/D67kRWw_cEEAAAAC/voz-dap-chym-dap-chym.gif"
        ]

        try:
            await ctx.guild.kick(user)

            # Creating Embed
            embed = discord.Embed(
                description = f"**Reason:** { reason }"
            )
            embed.set_author(
                name = f"{ user } has been kicked",
                url = user.avatar_url
            )
            embed.set_image(
                url = random.choice(kick_gif_list)
            )

            await ctx.send(embed = embed)

        except discord.errors.Forbidden:
            await ctx.send("I don't have permission to kick a Administrator.")
    
    @commands.command(aliases = ["ban"])
    async def _ban(self, ctx, user : discord.User, *, reason = None):
        reason = "Dumbass forgot to put a reason" if reason == None else reason
        author = ctx.message.author

        try:
            await ctx.guild.ban(user)

            # Creating Embed
            embed = discord.Embed(
                color = discord.Color.red(),
                description = f"**Ban Hammer** dropped on { user }"
            )
            embed.set_footer(
                text = f"Reason: { reason }",
                icon_url = author.avatar_url
            )

            await ctx.send(embed = embed)
        
        except discord.errors.Forbidden:
            await ctx.send("I don't have permission to ban a Administrator.")
    
    @commands.command(aliases = ["unban"])
    async def _unban(self, ctx, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        found = False
        for ban_entry in banned_users:
            user = ban_entry.banned_users

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                found = True
                await ctx.guild.unban(user)
                await ctx.send(f"**{ user }** has been unbanned")
        
        if found == False:
            await ctx.send("No one with that username is on the Ban List")

    @commands.command(aliases = ["mute"])
    async def _mute(self, ctx, member : discord.Member, *, reason = None):
        wait_time = 10 * 60 # 10 Minutes
        reason = "Dumbass forgot to put a reason" if reason == None else reason

        # Creating Embed
        embed = discord.Embed(
            description = f"**Reason:** { reason }"
        )
        embed.set_footer(
            text = "Unmute: 10 Minutes"
        )

        # Muting
        author = ctx.message.author
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await ctx.send(f"**{ author }** has been muted", embed = embed)

        # Unmuting (After 10 Minutes)
        await asyncio.sleep(wait_time)
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(f"**{ author }** has been unmuted")
    
    @commands.command(aliases = ["unmute"])
    async def _unmute(self, ctx, member : discord.Member, *, reason = None):
        reason = "Dumbass forgot to put a reason" if reason == None else reason
        author = ctx.message.author
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(f"**{ author }** has been unmuted")
        else:
            await ctx.send(f"**{ author }** is already unmuted")
    
    @commands.command(aliases = ["clear"])
    async def _clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount)
        success_msg = await ctx.send("I have deleted `{} {}`!".format(
            amount, 
            "messages" if amount > 1 else "message"
        ))
        wait_time = 2
        await asyncio.sleep(wait_time)
        await success_msg.delete()

def setup(bot):
    bot.add_cog(Moderation(bot))