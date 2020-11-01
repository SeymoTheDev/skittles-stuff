import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

class Developers(commands.Cog):

    def __int__(self, client):
        self.client = client










def setup(client):
    client.add_cog(Developers(client))