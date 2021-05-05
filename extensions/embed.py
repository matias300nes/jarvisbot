from discord.ext import commands
import discord

class Embed(commands.Cog):

    @commands.command()
    async def embed_example(self, ctx):
        """| shows an example embed """
        embed=discord.Embed(
        title="Text Formatting",
            url="https://realdrewdata.medium.com/",
            description="Here are some ways to format text",
            color=discord.Color.blue())
        #embed.set_author(name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://cdn-images-1.medium.com/fit/c/32/32/1*QVYjh50XJuOLQBeH_RZoGw.jpeg")
        embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
        embed.add_field(name="*Italics*", value="Surround your text in asterisks (\*)", inline=False)
        embed.add_field(name="**Bold**", value="Surround your text in double asterisks (\*\*)", inline=False)
        embed.add_field(name="__Underline__", value="Surround your text in double underscores (\_\_)", inline=False)
        embed.add_field(name="~~Strikethrough~~", value="Surround your text in double tildes (\~\~)", inline=False)
        embed.add_field(name="`Code Chunks`", value="Surround your text in backticks (\`)", inline=False)
        embed.add_field(name="Blockquotes", value="> Start your text with a greater than symbol (\>)", inline=False)
        embed.add_field(name="Secrets", value="||Surround your text with double pipes (\|\|)||", inline=False)
        embed.set_image(url = "https://image.freepik.com/vector-gratis/icono-robot-diseno-signo-bot-concepto-simbolo-chatbot-servicio-soporte-voz-bot-bot-soporte-linea-vector-stock-ilustracion_100456-34.jpg")
        embed.set_footer(text="Learn more here: realdrewdata.medium.com")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Embed(bot))