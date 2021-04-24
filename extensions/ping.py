from discord.ext import commands

@commands.command(help='Responds with a random ping')
async def ping(ctx):
    await ctx.channel.send("pong!")

def setup(bot):
    bot.add_command(ping)

