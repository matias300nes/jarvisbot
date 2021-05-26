from discord.ext import commands
import discord, random
from replit import db

class Talking(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f'\n\nLogged in as: {self.bot.user.name} - {self.bot.user.id}\nVersion: {discord.__version__}\n'
        )

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content.lower()
        bot_name = self.bot.user.name

        if msg != self.bot.user and str(bot_name) in msg:

            response = ''
            ##INTERACTIVE MODULE
            ##toma como trigger trigger_tema y da una respuesta de response_tema
            ##notar que tema en trigger_ y response_ debe ser igual
            for key in db:
                if any(word in msg for word in db[key]) and 'trigger_' in key:
                    new_key = key.replace('trigger_', 'response_')
                    response += random.choice(db[new_key])

            if response == '':
                response = '🕵️‍♂️ $help'

            await message.channel.send(response)

def setup(bot):
    bot.add_cog(Talking(bot))
