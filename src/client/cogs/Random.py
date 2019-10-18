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
    
    @commands.command()
    async def strawpoll(self, ctx, title: str, *options: str):
        await ctx.message.delete()

        data = {'title': title, 'options':  options}
        link = "https://www.strawpoll.me/api/v2/polls"

        get_poll = requests.post(link, json=data, headers={
                                 'Content-Type': 'application/json'})

        json = get_poll.json()

        message = 'The link to the strawpoll is https://strawpoll.me/{}'.format(
            json['id']
        )

        jsonData = {
            "title": "Strawpoll - {}".format(title),
            "description": message
        }

        try:
            requests.post('http://localhost:3000/strawpoll', json=jsonData)
        except Exception as e:
            print(e)