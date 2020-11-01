import qsbot
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='qs!')


@bot.event
async def on_ready():
    print('qs is on and ready to moderate :D')


@bot.event
async def on_member_join(member):
    await bot.send_message(member.server, "Welcome {0.mention}, How are you today?")


@bot.command(pass_context=True)
async def announce(ctx, channel: discord.TextChannel, *, msg):
    author = ctx.author
    await channel.send(f'An announcement has been made by {author}\n\n\n\n{msg}')


async def on_message(message):
    if message.content.startswith('meat'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))


@bot.command()
async def purge(ctx, amount=None):
    await ctx.channel.purge()


@bot.command(aliases=['newinst', 'buildnew'])
async def createnew(ctx, *, instance, limit=1):
    await ctx.send(f'Created {limit} new Instances of {instance}')

    userinstances = amount


@bot.command(aliases=['myinst', 'instances', 'myidata', 'userdata'])
async def myinstances(ctx):
    await ctx.author.send(f'you currently have {userinstances} instances.')


bot.run('NzcxODMxMjkyNTMzNjY5ODk4.X5x16A.0fQ7woFHqVsRBgxWdxwXyzrSpxA')
