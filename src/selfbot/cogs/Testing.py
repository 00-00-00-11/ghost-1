import discord
from discord.ext import commands
import requests


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testapi(self, ctx, *message):
        """For simple testing of API message send. If this fails, something has gone very wrong."""
        await ctx.message.delete()

        jsonData = {
            'title': 'Message Relay',
            'message': message
        }
        
        async with aiohttp.ClientSession() as session:
            await session.post('http://localhost:3000/message', json=jsonData)
