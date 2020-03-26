import sqlite3
import discord
from discord.ext import commands
token = open("token").read()
forbidden = "You're not allowed to use this command."

client = commands.AutoShardedBot(command_prefix = '.')

client.remove_command('help')
client.load_extension('about')
client.load_extension('eval')
client.load_extension('fun')

owners = [YOURID]

@client.event
async def on_ready():
    print('logged in as', client.user)
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name='you.'))

@client.command()
async def load(ctx, *, arg):
    if ctx.author.id in owners:
        client.load_extension(arg)
        await ctx.send(f"Loaded `{arg}`")
    else:
        await ctx.send(forbidden)

@client.command()
async def unload(ctx, *, arg):
    if ctx.author.id in owners:
        client.unload_extension(arg)
        await ctx.send(f"Unloaded `{arg}`")
    else:
        await ctx.send(forbidden)

@client.command()
async def reload(ctx, *, arg):
    if ctx.author.id in owners:
        client.unload_extension(arg)
        client.load_extension(arg)
        await ctx.send(f"Reloaded `{arg}`")
    else:
        await ctx.send(forbidden)

client.run(token)
