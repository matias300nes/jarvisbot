from discord.ext import commands
import discord
from replit import db

class Crud(commands.Cog):

    @commands.command()
    async def key_list(self, ctx):
        """| shows all the keys"""
        key_list = f'key_list = {db.keys()}'
        await ctx.send(key_list)

    @commands.command()
    async def get(self, ctx, key):
        """| shows all values of a key"""
        await ctx.send(f'{key} = {list(db[key])}')

    @commands.command()
    async def delete(self, ctx, key, *args):
        """| delete a key or multiple values from key"""
        if args:
            values = db[key]
            for value in args:
                values.remove(value)
            db[key] = values
        else:
            del db[key]

        await ctx.send(f'perfecto, eliminado!')

    @commands.command()
    async def add(self, ctx, key, *args):
        """| add key or multiple new values"""
        if key in db.keys():
            values = db[key]
            for value in args:
                values.append(value)
            db[key] = values
        else:
            if args:
                values = []
                for value in args:
                    values.append(value)
                db[key] = values  
            else:
                db[key] = []

        await ctx.send(f'perfecto, añadido!')

def setup(bot):
    bot.add_cog(Crud(bot))

