from discord.ext import commands
import random

@commands.command(help='jokes')
async def joke(ctx):
    document = open('jokes.txt')
    lines = document.read().splitlines()
    document.close()
    await ctx.channel.send(random.choice(lines))

def setup(bot):
    bot.add_command(joke)