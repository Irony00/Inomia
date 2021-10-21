import discord
from discord.ext import commands

class ReactionColorRoleEmbed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases = ["green"])
    async def _green(self, ctx):
        embed = discord.Embed(
            title = "Even Tempered 🌳", # Green
            color = discord.Color.green(),
            description = '''
                > ”Forget not that the earth delights to feel your bare feet and the winds long to play with your hair.” —Khalil Gibran 

                <@&900441187931021362> <@&900441248341565470> <@&900441284701986877> <@&900441387928002560> <@&900441437097840680>
            '''
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/cc/18/a5/cc18a5901d40c79d27a3c38584329956.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:green_deep:900501458598916187>")
        await message.add_reaction("<:green_pine:900501458821210172>")
        await message.add_reaction("<:green_olive:900501458926043136>")
        await message.add_reaction("<:green_fern:900501458816995358>")
        await message.add_reaction("<:green_light:900501458879918110>")
    
    @commands.command(aliases = ["blue"])
    async def _blue(self, ctx):
        embed = discord.Embed(
            title = "Waves ☁️", # Blue
            color = discord.Color.dark_blue(),
            description = '''
                > “Don’t worry if you’re making waves simply by being yourself. The moon does it all the time.”
                – Scott Stabile

                <@&900440885983076372> <@&900440930178433074> <@&900441018267209819> <@&900441061678280735> <@&900441107752681482>
            '''
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/d0/e2/a8/d0e2a8ae4195b8105ceb7477267367e1.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:blue_ocean:900501458628259892>")
        await message.add_reaction("<:blue_teal:900501458565357629>")
        await message.add_reaction("<:blue_sapphire:900501458905096212>")
        await message.add_reaction("<:blue_spruce_light:900501458909270046>")
        await message.add_reaction("<:blue_light:900501458766663690>")
    
    @commands.command(aliases = ["light"])
    async def _light(self, ctx):
        embed = discord.Embed(
            title = "Break Up 🖤", # White - Black
            description = '''
            > “Let’s loosen up some time and take a break to re-calibrate our life. We need no endless over-thinking, though. Let’s just connect the dots, set the scene, and steam ahead. (\"On a casual day without a tie\")” 
            ― Erik Pevernagie 

            <@&898162199896412200> <@&900440592222388295> <@&900440704650731550> <@&900440753795379200> <@&900440803925704746>
            ''',
            color = 0xFFFFFF
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/64/ce/9f/64ce9f3c2463b528dfba90720fed9ea5.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:black:900501458552778802>")
        await message.add_reaction("<:black_ebony:900501458842169374>")
        await message.add_reaction("<:black_crow:900501458594713640>")
        await message.add_reaction("<:white_smoke:900501458561138689>")
        await message.add_reaction("<:white_snow:900501458951208980>")
    
    @commands.command(aliases = ["purplepink"])
    async def _purplepink(self, ctx):
        embed = discord.Embed(
            title = "Juvenile ✨", # Purple - Pink
            color = discord.Color.purple(),
            description = '''
            > “There's something enchanted about night. All those heavenly bodies, shooting stars, the crescent moon, celestial phenomenon.” 
            —Luanne Rice

            <@&898651037647380480> <@&900442140189020240> <@&900442185118400542> <@&900442224599384175> <@&900442303360008232>
            '''
        )
        embed.set_image(
            url = "https://cutewallpaper.org/21/anime-fantasy-scenery/gif-sky-moon-space-purple-clouds-Magic-fantasy-scenery-.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:pp_wine:900501458854768730>")
        await message.add_reaction("<:pp_eggplant:900501458577928234>")
        await message.add_reaction("<:pp_mauve:900501458917670912>")
        await message.add_reaction("<:pp_pink:900501458405974048>")
        await message.add_reaction("<:pp_light:900501458515030027>")
    
    @commands.command(aliases = ["red"])
    async def _red(self, ctx):
        embed = discord.Embed(
            title = "Heart ❤️", # Red
            color = discord.Color.red(),
            description = '''
            > “I saw that you were perfect, and so I loved you. Then I saw that you were not perfect and I loved you even more.” 
            —Angelita Lim

            <@&900442475125145601> <@&900442530187968573> <@&900442574077186099> <@&900442650669379585> <@&900389156235120671>
            '''
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/9b/da/90/9bda90c406615bfb08c1deee5eac12f0.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:red_merlot:900501458825408542>")
        await message.add_reaction("<:red_berry:900501458586308630>")
        await message.add_reaction("<:red_apple:900501458800218163>")
        await message.add_reaction("<:red:900501459064475708>")
        await message.add_reaction("<:red_rose:900501458825388043>")

    @commands.command(aliases = ["orange"])
    async def _orange(self, ctx):
        embed = discord.Embed(
            title = "Twilight 🌇", # Orange
            color = discord.Color.orange(), 
            description = '''
            > “When your world moves too fast, and you lose yourself in the chaos, come sit with us together and enjoy the sunset.” 
            — Insomnia

            <@&900441486871650374> <@&900441654975139911> <@&900441738903187477> <@&900389158764314655> <@&900441821551923241>
            '''
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/a6/eb/2f/a6eb2f38b2323718b0e318ed2b59f57e.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:orange_tiger:900502881260670996>")
        await message.add_reaction("<:orange_merigold:900501458489860108>")
        await message.add_reaction("<:orange_honey:900501458829607012>")
        await message.add_reaction("<:yellow:900501459026714655>")
        await message.add_reaction("<:orange_light:900501458871549952>")
    
    @commands.command(aliases = ["cyan"])
    async def _cyan(self, ctx):
        embed = discord.Embed(
            title = "Aurora 🌌",
            color = discord.Color.blue(), # Cyan
            description = '''
            > “We all have great things on our bucket lists like skydiving, seeing the Northern Lights, etc, but what about simply falling in love? Isn’t that the most amazing thing we can do?” 
            – Walt Whitman
            
            <@&900496258261729311> <@&900496357377339422> <@&900496403082666064> <@&898164889116352543> <@&900496517985603625>
            '''
        )
        embed.set_image(
            url = "https://images.unsplash.com/photo-1568607689150-17e625c1586e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXwzNTE3MjB8fGVufDB8fHx8&w=1000&q=80"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:cyan_dark:900501458867351562>")
        await message.add_reaction("<:cyan_sea_green:900501458879905862>")
        await message.add_reaction("<:cyan_azure:900501458850570260>")
        await message.add_reaction("<:cyan:900501458800214056>")
        await message.add_reaction("<:cyan_light:900501458515025971>")

def setup(bot):
    bot.add_cog(ReactionColorRoleEmbed(bot))