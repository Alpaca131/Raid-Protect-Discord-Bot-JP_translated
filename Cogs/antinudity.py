import discord
import asyncio
import json

from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions

# ------------------------ COGS ------------------------ #


class AntiNudityCog(commands.Cog, name="わいせつな写真から保護します"):
    def __init__(self, bot):
        self.bot = bot

# ------------------------------------------------------ #

    @commands.command(name='antinudity',
                      aliases=["nudity", "porn"],
                      usage="<true/false>",
                      description="わいせつな写真を許可・禁止する設定をします。")
    @has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.member)
    @commands.guild_only()
    async def antinudity(self, ctx, antiNudity):

        antiNudity = antiNudity.lower()

        if antiNudity == "true":
            # Edit configuration.json
            with open("configuration.json", "r") as config:
                data = json.load(config)
                # Add modifications
                data["antiNudity"] = True
                newdata = json.dumps(data, indent=4, ensure_ascii=False)

            embed = discord.Embed(
                title=f"**保護が有効になりました**", description=f"わいせつな写真からの保護をする設定にしました。", color=0x2fa737)  # Green
        else:
            # Edit configuration.json
            with open("configuration.json", "r") as config:
                data = json.load(config)
                # Add modifications
                data["antiNudity"] = False
                newdata = json.dumps(data, indent=4, ensure_ascii=False)

            embed = discord.Embed(
                title=f"**保護が無効になりました**", description=f"わいせつな写真からの保護をしない設定にしました。", color=0xe00000)  # Red

        await ctx.channel.send(embed=embed)

        with open("configuration.json", "w") as config:
            config.write(newdata)

# ------------------------ BOT ------------------------ #


def setup(bot):
    bot.add_cog(AntiNudityCog(bot))
