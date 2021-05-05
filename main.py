import os
import discord
from keep_alive import keep_alive
import random
from replit import db
from discord.ext import commands

bot = commands.Bot(command_prefix="$")

initial_extensions = [
    'extensions.greetings',
    'extensions.ping',
    'extensions.joke',
    'extensions.crud',
    'extensions.embed',
    'extensions.tictactoe'
]

if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)

@bot.event
async def on_ready():
	print(
	    f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n'
	)

@bot.event
async def on_message(message):

    msg = message.content.lower()
    bot_name = bot.user.name

    if msg != bot.user and str(bot_name) in msg:

        response = ''
        ##INTERACTIVE MODULE
        ##toma como trigger trigger_tema y da una respuesta de response_tema
        ##notar que tema en trigger_ y response_ debe ser igual
        for key in db:
            if any(word in msg for word in db[key]) and 'trigger_' in key:
                new_key = key.replace('trigger_', 'response_')
                response += random.choice(db[new_key])

        if response == '':
            response = 'dime'

        await message.channel.send(response)

    await bot.process_commands(message)


keep_alive()

token = os.environ['DISCORD_BOT_SECRET']

bot.run(token)
