import discord
from discord.ext import commands

class ReactionColorRoleListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
        emoji_name = payload.emoji.name

        color_role_embeds_msg_id = {
            900511856974790666 : "green",
            900511903875489882 : "blue",
            900511948305731625 : "black_white",
            900512013627826217 : "purple_pink",
            900512058704015450 : "red",
            900512111329964052 : "orange",
            900512164064952330 : "cyan"
        }

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
            "ange_tiger" : discord.utils.get(guild.roles, name = "Tiger"),
            "ange_marigold" : discord.utils.get(guild.roles, name = "Merigold"),
            "ange_honey" : discord.utils.get(guild.roles, name = "Honey"),
            "yellow" : discord.utils.get(guild.roles, name = "Yellow"),
            "ange_light" : discord.utils.get(guild.roles, name = "Light Orange")
        }

        cyan_emoji_roles_table = {
            "cyan_dark" : discord.utils.get(guild.roles, name = "Dark Cyan"),
            "cyan_sea_green" : discord.utils.get(guild.roles, name = "Sea Green"),
            "cyan_azure" : discord.utils.get(guild.roles, name = "Azure"),
            "cyan" : discord.utils.get(guild.roles, name = "Cyan"),
            "cyan_light" : discord.utils.get(guild.roles, name = "Light Cyan")
        }

        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if message_id in color_role_embeds_msg_id:
            category = color_role_embeds_msg_id[message_id]
            
            if category == "green":
                role = green_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.add_roles(role)

            elif category == "blue":
                role = blue_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.add_roles(role)

            elif category == "black_white":
                role = white_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.add_roles(role)

            elif category == "purple_pink":
                role = purple_pink_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.add_roles(role)

            elif category == "red":
                role = red_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.add_roles(role)

            elif category == "orange":
                role = orange_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.add_roles(role)

            elif category == "cyan":
                role = cyan_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.add_roles(role)
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
        emoji_name = payload.emoji.name

        color_role_embeds_msg_id = {
            900511856974790666 : "green",
            900511903875489882 : "blue",
            900511948305731625 : "black_white",
            900512013627826217 : "purple_pink",
            900512058704015450 : "red",
            900512111329964052 : "orange",
            900512164064952330 : "cyan"
        }

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
            "orange_marigold" : discord.utils.get(guild.roles, name = "Merigold"),
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

        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        if message_id in color_role_embeds_msg_id:
            category = color_role_embeds_msg_id[message_id]
            
            if category == "green":
                role = green_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.remove_roles(role)

            elif category == "blue":
                role = blue_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.remove_roles(role)

            elif category == "black_white":
                role = white_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.remove_roles(role)

            elif category == "purple_pink":
                role = purple_pink_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.remove_roles(role)

            elif category == "red":
                role = red_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.remove_roles(role)

            elif category == "orange":
                role = orange_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.remove_roles(role)

            elif category == "cyan":
                role = cyan_emoji_roles_table[emoji_name]
                if member is not None:
                    await member.remove_roles(role)

def setup(bot):
    bot.add_cog(ReactionColorRoleListener(bot))