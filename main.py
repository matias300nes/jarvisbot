import os
import discord
from keep_alive import keep_alive
import random
from replit import db

from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="$")

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

initial_extensions = [
    'extensions.greetings',
    'extensions.ping',
    'extensions.joke',
    'extensions.crud',
]

if __name__ == '__main__':
	for extension in initial_extensions:
		bot.load_extension(extension)


@bot.event
async def on_ready():
	print(
	    f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n'
	)


def add_phrase(command):
	key = command.split(':', 1)[0]
	value = command.split(':', 1)[1]
	if key in db.keys():
		values = db[key]
		values.append(value)
		db[key] = values
	else:
		db[key] = [value]

	return f'perfecto, {key} : {value} añadido!'


def delete_phrase(command):

	if ':' in command:
		key = command.split(':', 1)[0]
		value = command.split(':', 1)[1]
		phrases = db[key]
		phrases.remove(value)
		db[key] = phrases
	else:
		del db[command]

	return 'eliminado!'


@bot.event
async def on_message(message):

	msg = message.content.lower()
	bot_name = bot.user.name

	if msg != bot.user and str(bot_name) in msg:
		response = ''

		##GET KEY_LIST
		if msg.startswith(f'${bot_name} key_list'):
      for any(word in msg for word in db[key]) and 'trigger'
        
      
        
		##GET A KEY'S VALUES
		elif msg.startswith(f'${bot_name} get '):
			command = msg.split(f'${bot_name} get ', 1)[1]
			response = f'{command} = {list(db[command])}'
		##DELETE A KEY OR VALUE
		elif msg.startswith(f'${bot_name} delete'):
			command = msg.split(f'${bot_name} delete ', 1)[1]
			response = delete_phrase(command)
		##ADD A KEY OR A VALUE
		elif msg.startswith(f'${bot_name} add '):
			command = msg.split(f'${bot_name} add ', 1)[1]
			response = add_phrase(command)
		else:
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
