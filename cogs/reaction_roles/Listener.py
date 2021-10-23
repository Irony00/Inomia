import discord
from discord.ext import commands

class Listener(commands.Cog):

    color_role_embeds_msg_id = {
        900597171051716608 : "green",
        900597195600953354 : "blue",
        900597217591693363 : "black_white",
        900597241960603648 : "purple_pink",
        900597400136200262 : "red",
        900597424828059728 : "orange",
        900597453613576192 : "cyan"
    }

    def __init__(self, bot):
        self.bot = bot

    async def give_take_color_role(self, payload, member, category, emoji_name, action):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

        green_emoji_roles_table = {
            "green_deep" : discord.utils.get(guild.roles, name = "Deep Green"),
            "green_pine" : discord.utils.get(guild.roles, name = "Pine"),
            "green_olive" : discord.utils.get(guild.roles, name = "Olive"),
            "green_fern" : discord.utils.get(guild.roles, name = "Fern"),
            "green_light" : discord.utils.get(guild.roles, name = "Light Green")
        }

        blue_emoji_roles_table = {
            "blue_ocean" : discord.utils.get(guild.roles, name = "Ocean"),
            "blue_teal" : discord.utils.get(guild.roles, name = "Teal"),
            "blue_sapphire" : discord.utils.get(guild.roles, name = "Sapphire"),
            "blue_spruce_light" : discord.utils.get(guild.roles, name = "Spruce"),
            "blue_light" : discord.utils.get(guild.roles, name = "Light Blue")
        }

        white_emoji_roles_table = {
            "black" : discord.utils.get(guild.roles, name = "Black"),
            "black_ebony" : discord.utils.get(guild.roles, name = "Ebony"),
            "black_crow" : discord.utils.get(guild.roles, name = "Crow"),
            "white_smoke" : discord.utils.get(guild.roles, name = "Smoke"),
            "white_snow" : discord.utils.get(guild.roles, name = "Snow")
        }

        purple_pink_emoji_roles_table = {
            "pp_wine" : discord.utils.get(guild.roles, name = "Wine"),
            "pp_eggplant" : discord.utils.get(guild.roles, name = "Egg Plant"),
            "pp_mauve" : discord.utils.get(guild.roles, name = "Mauve"),
            "pp_pink" : discord.utils.get(guild.roles, name = "Bright Lilace"),
            "pp_light" : discord.utils.get(guild.roles, name = "Light Purple") # Change this role name to Light Pink
        }

        red_emoji_roles_table = {
            "red_merlot" : discord.utils.get(guild.roles, name = "Merlot"),
            "red_berry" : discord.utils.get(guild.roles, name = "Berry"),
            "red_apple" : discord.utils.get(guild.roles, name = "Apple"),
            "red" : discord.utils.get(guild.roles, name = "Rose"),
            "red_rose" : discord.utils.get(guild.roles, name = "Red")
        }

        orange_emoji_roles_table = {
            "orange_tiger" : discord.utils.get(guild.roles, name = "Tiger"),
            "orange_merigold" : discord.utils.get(guild.roles, name = "Merigold"),
            "orange_honey" : discord.utils.get(guild.roles, name = "Honey"),
            "yellow" : discord.utils.get(guild.roles, name = "Yellow"),
            "orange_light" : discord.utils.get(guild.roles, name = "Light Orange")
        }

        cyan_emoji_roles_table = {
            "cyan_dark" : discord.utils.get(guild.roles, name = "Dark Cyan"),
            "cyan_sea_green" : discord.utils.get(guild.roles, name = "Sea Green"),
            "cyan_azure" : discord.utils.get(guild.roles, name = "Azure"),
            "cyan" : discord.utils.get(guild.roles, name = "Cyan"),
            "cyan_light" : discord.utils.get(guild.roles, name = "Light Cyan")
        }

        if category == "green":
            role = green_emoji_roles_table[emoji_name]
            if member is not None:
                if action == "give":
                    await member.add_roles(role)
                elif action == "take":
                    await member.remove_roles(role)

        elif category == "blue":
            role = blue_emoji_roles_table[emoji_name]
            if member is not None:
                if action == "give":
                    await member.add_roles(role)
                elif action == "take":
                    await member.remove_roles(role)

        elif category == "black_white":
            role = white_emoji_roles_table[emoji_name]
            if member is not None:
                if action == "give":
                    await member.add_roles(role)
                elif action == "take":
                    await member.remove_roles(role)

        elif category == "purple_pink":
            role = purple_pink_emoji_roles_table[emoji_name]
            if member is not None:
                if action == "give":
                    await member.add_roles(role)
                elif action == "take":
                    await member.remove_roles(role)

        elif category == "red":
            role = red_emoji_roles_table[emoji_name]
            if member is not None:
                if action == "give":
                    await member.add_roles(role)
                elif action == "take":
                    await member.remove_roles(role)
        
        elif category == "orange":
            role = orange_emoji_roles_table[emoji_name]
            if member is not None:
                if action == "give":
                    await member.add_roles(role)
                elif action == "take":
                    await member.remove_roles(role)
        
        elif category == "cyan":
            role = cyan_emoji_roles_table[emoji_name]
            if member is not None:
                if action == "give":
                    await member.add_roles(role)
                elif action == "take":
                    await member.remove_roles(role)

    async def clear_all_previous_color_roles(self, payload, member):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

        color_roles = [
            discord.utils.get(guild.roles, name = "Deep Green"),
            discord.utils.get(guild.roles, name = "Pine"),
            discord.utils.get(guild.roles, name = "Olive"),
            discord.utils.get(guild.roles, name = "Fern"),
            discord.utils.get(guild.roles, name = "Ocean"),
            discord.utils.get(guild.roles, name = "Teal"),
            discord.utils.get(guild.roles, name = "Sapphire"),
            discord.utils.get(guild.roles, name = "Spruce"),
            discord.utils.get(guild.roles, name = "Light Blue"),
            discord.utils.get(guild.roles, name = "Black"),
            discord.utils.get(guild.roles, name = "Ebony"),
            discord.utils.get(guild.roles, name = "Crow"),
            discord.utils.get(guild.roles, name = "Smoke"),
            discord.utils.get(guild.roles, name = "Snow"),
            discord.utils.get(guild.roles, name = "Wine"),
            discord.utils.get(guild.roles, name = "Egg Plant"),
            discord.utils.get(guild.roles, name = "Mauve"),
            discord.utils.get(guild.roles, name = "Bright Lilace"),
            discord.utils.get(guild.roles, name = "Light Purple"),
            discord.utils.get(guild.roles, name = "Merlot"),
            discord.utils.get(guild.roles, name = "Berry"),
            discord.utils.get(guild.roles, name = "Apple"),
            discord.utils.get(guild.roles, name = "Rose"),
            discord.utils.get(guild.roles, name = "Red"),
            discord.utils.get(guild.roles, name = "Tiger"),
            discord.utils.get(guild.roles, name = "Merigold"),
            discord.utils.get(guild.roles, name = "Honey"),
            discord.utils.get(guild.roles, name = "Yellow"),
            discord.utils.get(guild.roles, name = "Light Orange"),
            discord.utils.get(guild.roles, name = "Dark Cyan"),
            discord.utils.get(guild.roles, name = "Sea Green"),
            discord.utils.get(guild.roles, name = "Azure"),
            discord.utils.get(guild.roles, name = "Cyan"),
            discord.utils.get(guild.roles, name = "Light Cyan")
        ]

        for role in color_roles:
            if role in member.roles:
                await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if message_id in self.color_role_embeds_msg_id:
            category = self.color_role_embeds_msg_id[message_id]
            emoji_name = payload.emoji.name
            await self.clear_all_previous_color_roles(payload, member)
            await self.give_take_color_role(payload, member, category, emoji_name, "give")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if message_id in self.color_role_embeds_msg_id:
            category = self.color_role_embeds_msg_id[message_id]
            emoji_name = payload.emoji.name
            await self.give_take_color_role(payload, member, category, emoji_name, "take")

def setup(bot):
    bot.add_cog(Listener(bot))