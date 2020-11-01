import discord
import random
import os
from discord.ext import commands


client = commands.Bot(command_prefix = '-')




def owner(ctx):
    return ctx.author.id == 753066619693039687

@client.command()
@commands.check(owner)
async def latency(ctx):
    await ctx.send(f'{client.latency * 1000}ms')

@client.command()
async def lib(ctx):
    msg = await ctx.send('mes')
    ctx.message.edit(msg, 'epic')

@client.command()
async def giverole(ctx, role: discord.Role, user: discord.Member):
    await user.give_roles(role)
    await ctx.send(f'Successfully removed {role.mention} to {user.mention}')


@client.command(aliases=['sentancegen', 'rsen'])
async def randomsentance(ctx, *, log):
    responses = ['Sentance generation test 1.',
                 'random sentance generation 2.',]
    await ctx.send(f' Your sentance. Log = {log} || {random.choice(responses)}')

    @client.command()
    async def kick(ctx, *, member: discord.Member, reason=None):
        await member.kick(reason=reason)

    @client.command()
    async def ban(ctx, *, member: discord.Member, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    @client.command()
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}.')
                return

client.run('NzU5MjA2MDgzMTEzNTE3MTI3.X26Hww.dt3Bk1quUeuoIjjVI6onoX53DZY')