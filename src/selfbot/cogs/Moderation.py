import discord
from discord.ext import commands
from asyncio import sleep
import aiohttp
import asyncio


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

        async with aiohttp.ClientSession() as session:
            await session.post('http://localhost:3000/massmove')

    @commands.command()
    async def self_purge(self, ctx, amount: int):
        # The channel to be purged and the the selfbot user.
        channel = ctx.message.channel
        author = ctx.author

        # Checks if the message author is me.s
        def is_me(m):
            return m.author == self.bot.user

        # TODO: Refactor to be rate limited
        # This works for now... Want to make it so it doesnt get rate limited / look suspicious...
        deleted = await channel.purge(limit=amount, check=is_me)

        jsonData = {
            'title': 'Self Purge',
            'description': f'Deleted {len(deleted) + 1} messages(s)'
        }

        async with aiohttp.ClientSession() as session:
            await session.post('http://localhost:3000/purge', json=jsonData)
