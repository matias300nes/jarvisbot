from discord.ext import commands
import discord, asyncio, re

class Utils(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.active_rooms = []

    @commands.command()
    async def schedule(self, ctx):
        embed=discord.Embed(
            title="Martes 18",
            url="https://docs.google.com/spreadsheets/d/e/2PACX-1vS5-JAeZ_GkNt1KCAwi8uMZNuIwD2PjnIIr03poJFxmiLNh1NBIEPZCmhV_eQ-hgA/pubhtml",
            description="18/05/2021",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url="https://img-premium.flaticon.com/png/512/1497/1497835.png?token=exp=1621345455~hmac=a77f2a345261a27431024ecf74b0ec79")
        embed.add_field(name='Sistemas Operativos', value='14:30 - 20:00', inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def clean_rooms(self, ctx, *args):
        if not args:
            for room in self.active_rooms:
                await room.delete()
            self.active_rooms = []


    @commands.command()
    async def new_room(self, ctx, *args):
        """| channel_type name duration(int + s,m,h,d)"""

        channel_type = 'voice'
        name = "room {}".format(len(self.active_rooms))     
        duration = 40
        
        multiplicator = {
            's':1,
            'm':60,
            'h':3600,
            'd':86400,
        }

        form = re.compile("([0-9]+)([a-zA-Z]+)")

        for arg in args:
            if arg == 'voice' or arg == 'text':
                channel_type=arg
            elif form.match(arg):
                res = form.match(arg).groups()
                duration = int(res[0]) * int(multiplicator[res[1]])               
            else:
                name = arg
                
        print(f"new room: {name}\n type: {channel_type}, duration: {duration}") 

        guild=discord.utils.get(ctx.guild.categories, name='active rooms')
        if channel_type == 'voice':
            channel = await guild.create_voice_channel(name)
        else:
            channel = await guild.create_text_channel(name)

        self.active_rooms.append(channel)

        await asyncio.sleep(duration)

        try:
            self.active_rooms.remove(channel)
            await channel.delete()
        except:
            pass


def setup(bot):
    bot.add_cog(Utils(bot))