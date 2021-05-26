import os
from keep_alive import keep_alive
from discord.ext import commands
from extensions._REGISTER import initial_extensions

bot = commands.Bot(command_prefix="$")

if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

keep_alive()

token = os.environ['DISCORD_BOT_SECRET']

bot.run(token)

