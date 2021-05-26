from discord.ext import commands
import discord

class Games(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    def board(self, game):
        board = ''
        for row in range(3):
            for col in range(3):
                board += '{} '.format(game[row][col])
            board += '\n'  
        return board

    def check_winner(self, game):
        
        #horizontal checker
        for row in game:
            if row.count(row[0]) == len(row):
                return True
        
        #vertical checker
        for col in range(len(game)):
            check = []
            for row in game:
                check.append(row[col])
            if check.count(check[0]) == len(check):
                return True

        #diagonal + checker
        diags = []
        for col, row in enumerate(reversed(range(len(game)))):
            diags.append(game[row][col])
        if diags.count(diags[0]) == len(diags):
            return True

        #diagonal - checker
        diags = []
        for i in range(len(game)):
            diags.append(game[i][i])
        if diags.count(diags[0]) == len(diags):
            return True
            

    @commands.command()
    async def tictactoe(self, ctx, player : discord.User):
        """| play with another User (@user)"""

        player1 = ctx.author
        player2 = player
        current_player = player1
        game_over = False

        moves = [
            '1️⃣','2️⃣','3️⃣',
            '4️⃣','5️⃣','6️⃣',
            '7️⃣','8️⃣','9️⃣',
        ]
        game = [[moves[j] for j in range((i*3), (i*3+3))]for i in range(0, 3)]

        board = self.board(game)
                
        embed = discord.Embed(
            title = 'TIC TAC TOE :video_game:',
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url = current_player.avatar_url)
        embed.add_field(name = 'Current player:',value= current_player.display_name, inline=False)
        embed.add_field(name='Board' ,value=board , inline=False)
        embed.set_footer(text='{} vs {}'.format(player1.display_name, player2.display_name))

        message = await ctx.send(embed=embed)

        active_board = message.id

        for item in moves:
            await message.add_reaction(item)

        while(not game_over):

            def check(reaction, user):
                return not user.bot and reaction.message.id == active_board

            reaction, user = await self.bot.wait_for('reaction_add', timeout = 3600, check = check)
            await message.remove_reaction(reaction, user)

            move = reaction.emoji

            if user == current_player and move in moves:
                moves.remove(move)
                await message.remove_reaction(move, self.bot.user)

                for i in range(len(game)):
                    for j in range(len(game[i])):
                        if game[i][j] == move:
                            game[i][j] = ':x:' if current_player == player1 else ':o:'
                
                board = self.board(game)
            
                embed.remove_field(1)
                embed.insert_field_at(index = 1, name='Board' ,value=board , inline=False)

                winner = self.check_winner(game)

                if winner:
                    embed.remove_field(0)
                    embed.insert_field_at(index = 0, name = 'Winner :confetti_ball:',value= current_player.display_name, inline=False)
                    vs = f'{player1.display_name}🏆 vs {player2.display_name}' if current_player == player1 else f'{player1.display_name} vs {player2.display_name}🏆'
                    embed.set_footer(text=vs)
                    game_over = True
                elif not moves:
                    embed.remove_field(0)
                    embed.insert_field_at(index = 0, name = 'Game Over 🏳',value= 'Nobody wins', inline=False)
                    game_over = True
                else:
                    current_player = player2 if current_player == player1 else player1
                    embed.set_thumbnail(url = current_player.avatar_url)
                    embed.remove_field(0)
                    embed.insert_field_at(index = 0, name = 'Current player:',value= current_player.display_name, inline=False)

                await message.edit(embed=embed)



def setup(bot):
    bot.add_cog(Games(bot))