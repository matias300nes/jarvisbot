from discord.ext import commands
import discord

class Crud(commands.Cog):

    @commands.comand()
    async def deb(ctx):
        await ctx.send('its working')

def setup(bot):
    bot.add_cog(Crud(bot))