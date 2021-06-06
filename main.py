import os
import discord
from keep_alive import keep_alive
from discord.ext import commands
from extensions._REGISTER import initial_extensions

activity=discord.Activity(
    type=discord.ActivityType.listening, name="$help"
)

bot = commands.Bot(command_prefix="$", activity=activity)

if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

keep_alive()

token = os.environ['DISCORD_BOT_SECRET']

bot.run(token)

