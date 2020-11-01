import discord
from discord.ext import commands

class codecmds(commands.Cog):

    def __int__(self, client):
        self.client = client


    @commands.command()
    async def log(self, ctx):
        await ctx.send('Log, Most recent log -----> Message sent @ nil')

    @commands.command(aliases=['mods','lib()'])
    async def modules(self, ctx):
        await ctx.send('There is only 1 mod available currently. sad. i know.')



def setup(client):
    client.add_cog(codecmds(client))