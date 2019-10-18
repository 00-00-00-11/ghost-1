import discord
from discord.ext import commands
from asyncio import sleep
import requests


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mass_move(self, ctx, fromChannel: discord.VoiceChannel, toChannel: discord.VoiceChannel):

        await ctx.message.delete()

        vc_members = fromChannel.members
        for i in range(len(vc_members)):
            # Changed the voice channel of all the members in the role and then sleeps for half a second so it doesnt get rate limited.
            await vc_members[i].edit(voice_channel=toChannel)
            await sleep(0.5)

        try:
            requests.post('http://localhost:3000/massmove')
        except Exception as e:
            print(e)