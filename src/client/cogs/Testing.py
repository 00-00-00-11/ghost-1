import discord
from discord.ext import commands
import requests


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testapi(self, ctx, msg='Hi'):
        """For testing API."""

        jsonData = {
            'msg': msg
        }

        try:
            requests.post('http://localhost:3000/message', json=jsonData)
        except Exception as e:
            print(e)
        
        print('request sent from client')