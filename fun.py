import discord
import asyncio
import requests as r
import random
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def howgay(self, ctx, member: discord.Member=None):
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.5)
        if member:
            embed = discord.Embed(
                title = 'Gay meter result',
                description = f'{member.mention} is {random.randint(0, 100)}% gay!',
                color = discord.Color(9436758)
            )
        await ctx.send(embed=embed)

    @commands.command()
    async def howlesbian(self, ctx, member: discord.Member=None):
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.5)
        if member:
            return await ctx.send(f'{member.mention} is {random.randint(0, 100)}% lesbian!')
        await ctx.send('Please mention someone!')

    @commands.command()
    async def cat(self, ctx):
        cat = r.get('https://aws.random.cat/meow').json()   
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.5)
        embed = discord.Embed(
            title = 'Meow! 🐱',
            color = discord.Color(9436758)
        )
        embed.set_image(url=cat['file'])
        await ctx.send(embed=embed)

    @commands.command()
    async def dog(self, ctx):
        dog = r.get('https://random.dog/woof.json').json()
        await ctx.channel.trigger_typing()
        await asyncio.sleep(0.5)
        embed = discord.Embed(
            title = 'Woof! 🐶',
            color = discord.Color(9436758)
        )
        embed.set_image(url=dog['url'])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(fun(client))
