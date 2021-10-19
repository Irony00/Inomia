import random
import asyncio
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["warn"])
    @commands.has_permissions(manage_roles = True, ban_members = True)
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
    @commands.has_permissions(kick_members = True)
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
    @commands.has_permissions(ban_members = True)
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
    @commands.has_permissions(ban_members = True)
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
    @commands.has_permissions(manage_roles = True)
    async def _mute(self, ctx, member : discord.Member, *, reason = None):
        wait_time = 10 * 60
        reason = "Dumbass forgot to put a reason" if reason == None else reason

        embed = discord.Embed(
            description = f"**Reason:** { reason }"
        )
        embed.set_footer(
            text = "Unmute: 10 Minutes"
        )

        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        await ctx.send(f"**{ member }** has been muted", embed = embed)

        await asyncio.sleep(wait_time)
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(f"**{ member }** has been unmuted")
    
    @commands.command(aliases = ["unmute"])
    @commands.has_permissions(manage_roles = True)
    async def _unmute(self, ctx, member : discord.Member, *, reason = None):
        reason = "Dumbass forgot to put a reason" if reason == None else reason
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(f"**{ member }** has been unmuted")
        else:
            await ctx.send(f"**{ member }** is already unmuted")
    
    @commands.command(aliases = ["clear"])
    @commands.has_permissions(manage_messages = True)
    async def _clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount)
        success_msg = await ctx.send("I have deleted `{} {}`!".format(
            amount, 
            "messages" if amount > 1 else "message"
        ))
        wait_time = 2
        await asyncio.sleep(wait_time)
        await success_msg.delete()
    
    @commands.command(aliases = ["lock"])
    @commands.has_permissions(manage_channels=True)
    async def _lock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(
            ctx.guild.default_role, 
            overwrite=overwrite
        )
        await ctx.send('Channel locked.')
    
    @commands.command(aliases = ["unlock"])
    @commands.has_permissions(manage_channels=True)
    async def _unlock(self, ctx, channel : discord.TextChannel=None):
        channel = channel or ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(
            ctx.guild.default_role, 
            overwrite=overwrite
        )
        await ctx.send('Channel unlocked.')

def setup(bot):
    bot.add_cog(Moderation(bot))