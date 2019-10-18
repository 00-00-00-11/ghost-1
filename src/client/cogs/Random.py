from discord.ext import commands
from utils.checks import embed_perms
import discord
import random
import requests

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, dice: str):
        await ctx.message.delete()

        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))

        jsonData = {
            "description": result
        }

        try:
            requests.post('http://localhost:3000/roll', json=jsonData)
        except Exception as e:
            print(e)