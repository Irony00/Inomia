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
        await message.add_reaction("<:green_deep:900592778168369172>")
        await message.add_reaction("<:green_pine:900592777891569665>")
        await message.add_reaction("<:green_olive:900592778311004240>")
        await message.add_reaction("<:green_fern:900592777908338729>")
        await message.add_reaction("<:green_light:900592778180960307>")
    
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
        await message.add_reaction("<:blue_ocean:900592777920921630>")
        await message.add_reaction("<:blue_sapphire:900592777811861515>")
        await message.add_reaction("<:blue_teal:900592778046738472>")
        await message.add_reaction("<:blue_spruce_light:900592777862213662>")
        await message.add_reaction("<:blue_light:900592777786687488>")
    
    @commands.command(aliases = ["light"])
    async def _light(self, ctx):
        embed = discord.Embed(
            title = "Break Up 🖤", # White - Black
            description = '''
> “Let’s loosen up some time and take a break to re-calibrate our life. We need no endless over-thinking, though. Let’s just connect the dots, set the scene, and steam ahead. (\"On a casual day without a tie\")” 
― Erik Pevernagie 

<@&900440430041251901> <@&900440592222388295> <@&900440704650731550> <@&900440753795379200> <@&900440803925704746>
            ''',
            color = 0xFFFFFF
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/64/ce/9f/64ce9f3c2463b528dfba90720fed9ea5.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:black:900592777539231814>")
        await message.add_reaction("<:black_ebony:900592777665065000>")
        await message.add_reaction("<:black_crow:900592777686057000>")
        await message.add_reaction("<:white_smoke:900592778466185246>")
        await message.add_reaction("<:white_snow:900592778122244128>")
    
    @commands.command(aliases = ["purplepink"])
    async def _purplepink(self, ctx):
        embed = discord.Embed(
            title = "Juvenile ✨", # Purple - Pink
            color = discord.Color.purple(),
            description = '''
> “There's something enchanted about night. All those heavenly bodies, shooting stars, the crescent moon, celestial phenomenon.” 
—Luanne Rice

<@&900442071507292201> <@&900442140189020240> <@&900442185118400542> <@&900442224599384175> <@&900442303360008232>
            '''
        )
        embed.set_image(
            url = "https://cutewallpaper.org/21/anime-fantasy-scenery/gif-sky-moon-space-purple-clouds-Magic-fantasy-scenery-.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:pp_wine:900592778529112114>")
        await message.add_reaction("<:pp_eggplant:900592778357141564>")
        await message.add_reaction("<:pp_mauve:900592778436833340>")
        await message.add_reaction("<:pp_pink:900592778139013161>")
        await message.add_reaction("<:pp_light:900592778478768178>")
    
    @commands.command(aliases = ["red"])
    async def _red(self, ctx):
        embed = discord.Embed(
            title = "Heart ❤️", # Red
            color = discord.Color.red(),
            description = '''
> “I saw that you were perfect, and so I loved you. Then I saw that you were not perfect and I loved you even more.” 
—Angelita Lim

<@&900442475125145601> <@&900442530187968573> <@&900442574077186099> <@&900442650669379585> <@&900442608831180800>
            '''
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/9b/da/90/9bda90c406615bfb08c1deee5eac12f0.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:red_merlot:900592778445209630>")
        await message.add_reaction("<:red_berry:900592778537484288>")
        await message.add_reaction("<:red_apple:900592778411671613>")
        await message.add_reaction("<:red_rose:900592778617159770>")
        await message.add_reaction("<:red:900592778470367242>")

    @commands.command(aliases = ["orange"])
    async def _orange(self, ctx):
        embed = discord.Embed(
            title = "Twilight 🌇", # Orange
            color = discord.Color.orange(), 
            description = '''
> “When your world moves too fast, and you lose yourself in the chaos, come sit with us together and enjoy the sunset.” 
— Insomnia

<@&900441486871650374> <@&900441654975139911> <@&900441738903187477> <@&900441776807092245> <@&900441821551923241>
            '''
        )
        embed.set_image(
            url = "https://i.pinimg.com/originals/a6/eb/2f/a6eb2f38b2323718b0e318ed2b59f57e.gif"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:orange_tiger:900596335848357928>")
        await message.add_reaction("<:orange_merigold:900592778306801676>")
        await message.add_reaction("<:orange_honey:900592778197753866>")
        await message.add_reaction("<:yellow:900592778793324564>")
        await message.add_reaction("<:orange_light:900592778210324500>")
    
    @commands.command(aliases = ["cyan"])
    async def _cyan(self, ctx):
        embed = discord.Embed(
            title = "Aurora 🌌",
            color = discord.Color.blue(), # Cyan
            description = '''
> “We all have great things on our bucket lists like skydiving, seeing the Northern Lights, etc, but what about simply falling in love? Isn’t that the most amazing thing we can do?” 
– Walt Whitman

<@&900496258261729311> <@&900496357377339422> <@&900496403082666064> <@&900496474297745418> <@&900496517985603625>
            '''
        )
        embed.set_image(
            url = "https://images.unsplash.com/photo-1568607689150-17e625c1586e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxjb2xsZWN0aW9uLXBhZ2V8MXwzNTE3MjB8fGVufDB8fHx8&w=1000&q=80"
        )
        message = await ctx.send(embed = embed)
        await message.add_reaction("<:cyan_dark:900592777971245076>")
        await message.add_reaction("<:cyan_sea_green:900592777782501417>")
        await message.add_reaction("<:cyan_azure:900592777623130164>")
        await message.add_reaction("<:cyan:900592777711194145>")
        await message.add_reaction("<:cyan_light:900592777996435487>")

def setup(bot):
    bot.add_cog(ReactionColorRoleEmbed(bot))