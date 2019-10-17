import discord
from discord.ext import commands
import requests


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testapi(self, ctx, *message):
        """For simple testing of API message send. If this fails, something has gone very wrong."""

        jsonData = {
            'title': 'Message Relay',
            'message': message
        }

        try:
            requests.post('http://localhost:3000/message', json=jsonData)
        except Exception as e:
            print(e)