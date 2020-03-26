import discord
from discord.ext import commands

class about(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            color = discord.Color(9436758)
        )

        embed.set_author(name='Help:', icon_url=self.bot.user.avatar_url)
        embed.add_field(inline=False, name='4Fun', value='> `howgay (@mention)`, `cat`, `dog,`')
        embed.add_field(inline=False, name='About', value='> `ping`')

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f':ping_pong: | **Pong!** `{round(self.bot.latency * 1000)}ms`')

def setup(client):
    client.add_cog(about(client))
