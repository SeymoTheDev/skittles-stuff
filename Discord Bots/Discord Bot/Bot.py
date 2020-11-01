import random
import os
import discord
import string
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix='S-')

# Something for boys who want among us in disc :)

N = 5

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))


# Gives the boy some variety
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="S-help || S-runtime"))


print(f'Logged in as the bot lmao')


# Commands. EZ
@client.command()
async def e(ctx):
    await ctx.send('e')


@client.command()
async def abc(ctx):
    await ctx.send('abcdefghijklmnopqrstuvwxyz // Why dont you know your abcs?')


@client.event
async def on_member_joined(ctx, *, member):
    await ctx.send(f'member, {member} has joined.')


@client.event
async def on_bot_joined(ctx, *, bot):
    await ctx.send(f'{bot} has joined the server.')


@client.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f'{msg}')


@client.command(pass_context=True)
async def dmt(ctx, user: discord.Member, *, msg, ):
    await ctx.message.delete()
    await user.send(f'{msg}')


@client.command(pass_context=True)
async def punch(ctx, user: discord.Member):
    punchrep = [f'Woww {ctx.author} punched {user} in the face.... you alright?',
                f'{user} Dodges {ctx.author}s Attack On them!!', f'{ctx.author} was the imposter.',
                'Dead Body Reported! Discuss..', f'{ctx.author} just got reversed by {user}',
                f'{user} Was sent to the firey pits of hell.',
                f'Hey... hey {user}, Look into the sky\n{user}: Okay\n***PUNCH***',
                f'{user} was punched into the ranch.', f'{ctx.author} sent {user} to heaven!.... but they later fell '
                                                       f'back down and cracked their neck. oh well.',
                f'Hey {user}..\n {user}: yeah?\n{ctx.author} said theyre sorry.\n{user}: Really?\nNo.\n{ctx.author} kills {user}.',
                f'{user} fell out of the world.',
                f'{user}: *on phone*\nalso {user}: *touches a spoiler on discord*\n{ctx.author}: *they did it. they touched it they are now the killer queen.*\n{user}: I FEEL SO POWERFUL! SO POWERFUL IMA THROW THIS BALL OUT THE WINDOW!\n**explosion and blood spatter**\n{ctx.author}: Wait it doesnt work like that-,'
                f'{user} Disconnected', f'haha funny jojo meme', f'as {ctx.author} punches {user}, {user} combat logs '
                                                                 f'and {ctx.author} gets so mad they punch a wall.',
                f'{ctx.author} you are an impostor.\n{ctx.author}: *doesnt do keys*\n{user}: tries to go to the emergency button but {ctx.author} stabs them.\nGreen And yellow: uhh\n\n\n\n{ctx.author} was the impostor.']

    await ctx.send(random.choice(punchrep))


@client.command(pass_context=True)
async def IorC(ctx):
    imp = ['shhh, Youre the imposter!', 'Youre a crewmate. Complete tasks around the ship and win the game',
           'Disconnected: pinged Servers 69 times got EOF']

    await ctx.author.send(random.choice(imp))


@client.command(pass_context=True)
async def mem(ctx):
    clan = ['Exotic Anims', 'DG anims', 'Bow', 'Ink on Toast', 'Big Animator', 'Dusk', 'Kurama X', 'Halo', 'Mercy',
            'Nano', 'SOMA', 'Vlad', 'meow meow']

    await ctx.send(random.choice(clan))


@client.command(pass_context=True)
async def code(ctx):
    code = ['your code is R8Y7B', 'your code is M0W6Z', 'your code is I32Y7', 'your code is SQ3S2',
            'your code is HC2G4', 'your code is DR97I']
    await ctx.author.send(random.choice(code))  # Lets user know their code
    await ctx.author.send('Let your friends know that so you can all play together!')


@client.command(pass_context=True)
async def GhostpingUser(ctx, user: discord.Member):
    await ctx.message.delete()
    await ctx.send('shhhhhh :)')


@client.command()
async def giveroles(ctx, role: discord.Role, user: discord.User):
    await user.add_roles(role)
    await ctx.send(f'Roles successfully added to {user}')


@client.command(pass_context=True)
async def uptime(ctx):
    await ctx.send(
        'This bot is on all week long, until the weekend, the weekend is where the bot will get huge '  # Sends the updates message to the ctx.author (command author )
        'updates, '
        'making it better and better over time.')


emoji = '\N{THUMBS UP SIGN}'


@client.command()
async def rr(ctx):
    message = await ctx.send('emoji should pop up')
    await message.add_reaction(emoji)


client.run('NzcxMDI1MDMyOTg5NjM4Njg2.X5mHBA.ZXY-81sG6fT0JoB7Q7luRsJp8Jk')
