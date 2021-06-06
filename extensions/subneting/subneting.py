from discord.ext import commands
from ipaddress import IPv4Address
from .net import Net

class Subneting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mask_type(self, ctx, mask):
        mask_type = mask.count('255')
        await ctx.send(mask_type)

    @commands.command()
    async def ip_sum(self, ctx, address, num):

        sum = Net.ip_sum(address=address, num=num)

        await ctx.send(sum)

    @commands.command()
    async def subnet(self, ctx, ip, mask, subnets_needed = None, *hosts_needed):

        my_net = Net(ip, mask)

        subnets = my_net.subnets

        await ctx.send(subnets)


def setup(bot):
    bot.add_cog(Subneting(bot))