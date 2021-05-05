from discord.ext import commands
import discord


class Tictactoe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.player1 = None
        self.player2 = None
        self.current_player = self.player1
    
    def next_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id != self.bot.user.id:
            move = payload.emoji
            print('user has reacted!! move: {}'.format(move))

    @commands.command()
    async def playwith(self, ctx, player2 : discord.User):
        self.player1 = ctx.author
        self.player2 = player2

        board = ":one: :two: :three: \n :four: :five: :six: \n :seven: :eight: :nine: \n"
                
        embed = discord.Embed(
            title = 'TIC TAC TOE :video_game:',
            color=discord.Color.blue()
        )
        
        embed.set_thumbnail(url = self.player1.avatar_url)
        embed.add_field(name = 'Current player:',value= self.player1.display_name, inline=False)

        embed.add_field(name='Board' ,value=board , inline=False)

        embed.set_footer(text='{} vs {}'.format(self.player1.display_name, self.player2.display_name))

        message = await ctx.send(embed=embed)

        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')
        await message.add_reaction('5️⃣')
        await message.add_reaction('6️⃣')
        await message.add_reaction('7️⃣')
        await message.add_reaction('8️⃣')
        await message.add_reaction('9️⃣')


    @commands.command()
    async def whoisplaying(self, ctx):       
        await ctx.send('players are: {}, {}'.format(self.player1, self.player2))


def setup(bot):
    bot.add_cog(Tictactoe(bot))