import discord
from discord.ext import commands
import requests


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, msg='Hi'):
        """For testing API."""

        # Delete message before doing anything
        await ctx.message.delete()

        jsonData = {
            'msg': msg
        }

        try:
            requests.post('https://localhost:5000/testing', json=jsonData)
        except Exception as e:
            print(e)
        
        print('request sent from client')