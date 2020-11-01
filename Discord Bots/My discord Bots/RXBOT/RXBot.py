import discord
import random
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='RX!')


@client.command()
async def members(ctx):
    print(f'{ctx.author} Requested to see all clan members using RXmembers.')
    await ctx.send('clan members here')


@client.event
async def on_ready(ctx):
    await ctx.send('RXBot Reloaded.')
    print('Artificial User Logged in.')


@client.command()
async def clear(ctx):
    discord.purge(ctx)
    ctx.send('yes')


client.run('NzcxNDAyNjcyMTg0MDk4ODI3.X5rmuQ.DmYkKuZ7JoJ3IZJQjFv1Z8hLO2k')
