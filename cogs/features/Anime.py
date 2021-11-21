import random
import discord
from discord.ext import commands
from RedditReader import Subreddit

anime_quotes = ["People’s lives don’t end when they die. It ends when they lose faith.",
               "The only thing we’re allowed to do is believe that we won’t regret the choice we made.",
               "I don’t care if no one like me, I wasn’t created in this world to entertain everyone." ,
               "Life is not a game of luck. If you wanna win, work hard.",
               "If you wanna stop this, then stand up! Because I’ve just got one thing to say to you! Never forget who you want to become!",
               "Remember that everyone you meet is afraid of something, loves something and has lost something.",
               "If you can’t find a reason to fight, then you shouldn’t be fighting.",
               "Because people don’t have wings, the look for ways to fly.",
               "As long as you laugh at people’s suffering, your goal will always be out of reach. If you never want to be defeated, you must first learn your own weakness, and always be kind.",
               "To know sorrow is not terrifying. What is terrifying is to know you can’t go back to happiness you could have.",
               "Whatever you lose, you’ll find it again. But what you throw away you’ll never get back.",
               "Be someone’s light when they are hopeless.",
               "Push through the pain, giving up hurts more.",
               "You can die anytime, but living takes true courage.",
               "There are no regrets. If one can be proud of one’s life, one should not wish for another chance." ,
               "If you don’t like your destiny, don’t accept it. Instead, have the courage to change it the way you want it to be.",
               "People who can’t throw something important away, can never hope to change anything.",
               "I yearn for true gender equality. I have no patience for one who talks about female privilege when it suits them, and then complains about someone “not being a man” when it’s convenient.",
               "No matter how hard or impossible it is, never lose sight of your goal.",
               "There was no place for me, so i had to make one for myself, and then i realized, i had a place, but i was the only one in it. I didn’t know any other way to live.",
               "Human beings are strong because we can change ourselves.",
               "I have no fear of death. It just means dreaming in silence. A dream that lasts for eternity.",
               "It will do no good to fight with hate in your heart.",
               "If there is the will, then there is hope.",
               "A life that lives without doing anything is the same as a slow death.",
               "The universe has a beginning, but no end. — Infinity. Stars, too, have their own beginnings, but their own power results in their destruction. — Finite.",
               "If you want to grant your own wish, then you should clear your own path to it."
               ]
"""
waifu = ["https://cdn.discordapp.com/attachments/902148232346497055/910401876384690186/kanao.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910401942335922176/anime-girls-hayasaka-ai-hd-wallpaper-preview-1.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910401942612750386/shinobu-sword.jfif_-1.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910402061974249502/Hinata-Hyuuga-0oADZx5CL-b.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910402205251670038/de7hvu6-6b974784-3ae2-48c5-920d-d063efcce5d1.png",
        "https://cdn.discordapp.com/attachments/902148232346497055/910402446294138921/ede0e8f312968865.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910402772678094888/maxresdefault.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910402785269411890/nami-ships-2-1024x576H-scaled-1200x900.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910404963992207360/Screenshot_20211117-111405_Google.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910405135472152656/1118aff26fd22e5ba8d241149f5b57c1.jpg",
        "https://cdn.discordapp.com/attachments/902148232346497055/910405436467982366/aGpyxA6_460s.jpg",
        "https://media.discordapp.net/attachments/902148232346497055/910419935602294785/Screenshot_20211117-120818_Google.jpg",
        "https://media.discordapp.net/attachments/902148232346497055/910419953243525150/764-7648266_sakura-haruno-sasuke-uchiha-naruto-sasusaku-sakura-haruno.png",
        "https://media.discordapp.net/attachments/902148232346497055/910420872748236850/Screenshot_20211117-121724_Google.jpg",
        "https://media.discordapp.net/attachments/902148232346497055/910448660800753674/jhjsdbruohq51.png",
        "https://media.discordapp.net/attachments/902148232346497055/910448689452036106/p0irsj6gwgk51.png",
        "https://media.discordapp.net/attachments/902148232346497055/910448701095424000/34h3n4v8v9171.jpg",
        "https://media.discordapp.net/attachments/902148232346497055/910448717063147550/gcapy3u3wru51.png",
        "https://media.discordapp.net/attachments/902148232346497055/910448739737550938/16kv08wn7lx61.png",
        "https://media.discordapp.net/attachments/902148232346497055/910448963499491358/5hwtp2dwmkd71.png",
        "https://media.discordapp.net/attachments/902148232346497055/910448964237672448/ekp3i7426an71.jpg",
        "https://media.discordapp.net/attachments/902148232346497055/910448979358121984/4yo8d5uw5az41.jpg",
        "https://media.discordapp.net/attachments/902148232346497055/910449010245005342/ucC8yf7.jpg",
        "https://media.discordapp.net/attachments/902148232346497055/910449010639245332/27450f63652e69af8ced66791ab2a424.jpg"]
"""

"""
husbando = ["https://cdn.discordapp.com/attachments/902148232346497055/910405573604962305/8c2d908a1de6d4a402cb614a6f1d97a2.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405573827252284/650b241d5d62a6794ad2f739ef3734a7.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405574032752680/1d893e7941fe52525e896d567767cf98.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405613182418984/9452cee3f780cf6aedea4dc5cb96907d.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405613425676288/d09f48ac255876d8fc72a3991df72925.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405613606010880/69c43d6cf26a092675a79316d33906ec.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405659110039603/9808db1db2bacbd828b98d1b48e153e0.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405659311345687/1c820265c37eddd0086599586fd0c27b.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405659525267516/e9705c9c51e53e65c0ee183442635547.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405686964412456/07a1f0987fc69c04273d18cc95aaf9c5.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405687153164328/90065dd28f376554311d8f0b132519d0.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910405687446732810/7e9090859b7a0c4540ab23fbda373f16.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910408667642335282/Painter_of_the_Night_-_Sezon_iki_-_Cilt_2.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910408668841922570/Unknown-2.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910408669873717288/Unknown-3.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910408672243490836/QUIN_on_Twitter.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910408673212399626/Unknown.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910408673988329482/Unknown-4.jpg",
           "https://cdn.discordapp.com/attachments/902148232346497055/910408676110643220/on_Twitter.png",
           "https://media.discordapp.net/attachments/902148232346497055/910417538914062376/Hot_Anime_Guys_book_1_-_Haruka_Nanase.jpg",
           "https://media.discordapp.net/attachments/902148232346497055/910417568714616873/Imagenes_ZoSan_-_65.jpg", # Cropping needed for thie Image
           "https://media.discordapp.net/attachments/902148232346497055/910417591368028230/Jujutsu_Kaisen-_A_Feiticeira.jpg"]
"""

class AnimeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def animeme(self, ctx):
        meme = Subreddit("Animemes")
        meme.get_random()
        url = meme.url
        title = meme.title
        upvotes = meme.upvotes
        comments = meme.comments
        em = discord.Embed(title=title, colour=discord.Colour.green())
        em.set_image(url=url)
        em.set_footer(text=f"powered by Inomia Devs | {upvotes} votes | {comments} comments")
        msg = await ctx.send(embed=em)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        
    @commands.command(aliases=['news','aninews'])
    async def anime_news(self, ctx):
        news = Subreddit("animenews")
        news.get_random()
        url = news.url
        title = news.title
        upvotes = news.upvotes
        comments = news.comments
        em = discord.Embed(title=title, colour=discord.Colour.green())
        em.set_image(url=url)
        em.set_footer(text=f"powered by Inomia Devs | {upvotes} votes | {comments} comments")
        msg = await ctx.send(embed=em)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
        
    @commands.command(aliases=['quote','quotes','aniquote'])
    async def anime_quotes(self, ctx):
        em = discord.Embed(title="Anime Quotes", colour = discord.Colour.red())
        em.set_footer(text = random.choice(anime_quotes))
        await ctx.send(embed=em)
        
    @commands.command()
    async def waifu(self, ctx):
        #im = random.choice(waifu)
        waifu = Subreddit("waifu")
        waifu.get_random()
        url = waifu.url
        title = waifu.title
        upvotes = waifu.upvotes
        comments = waifu.comments
        em = discord.Embed(title=title, colour = discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f"powered by Inomia Devs | {upvotes} votes | {comments} comments")
        #em.set_image(url=im)
        await ctx.send(embed=em)

    @commands.command()
    async def husbando(self, ctx):
        hub = Subreddit("Husbando")
        hub.get_random()
        url = hub.url
        title = hub.title
        upvotes = hub.upvotes
        comments = hub.comments
        em =  discord.Embed(title=title, colour = discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f"powered by Inomia Devs | {upvotes} votes | {comments} comments")
        #em.set_image(url=random.choice(husbando))
        await ctx.send(embed=em)
    
    @commands.command()
    async def hentai(self, ctx):
        insomnia_guild_id = 898127603309899806
        if ctx.message.guild.id == insomnia_guild_id:
            await ctx.send("This feature has been **disabled** in this server.")
            return
          
        hentai = Subreddit("hentai")
        hentai.get_random()
        url = hentai.url
        title = hentai.title
        upvotes = hentai.upvotes
        comments = hentai.comments
        em =  discord.Embed(title=title, colour = discord.Colour.blue())
        em.set_image(url=url)
        em.set_footer(text=f"powered by Inomia Devs | {upvotes} votes | {comments} comments")
        #em.set_image(url=random.choice(husbando))
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(AnimeCog(bot))
