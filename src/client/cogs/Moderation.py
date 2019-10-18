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
    
    @commands.command()
    async def self_purge(self, ctx, amount: int):
        # The channel to be purged and the the selfbot user.
        channel = ctx.message.channel
        author = ctx.author

        # Checks if the message author is me.s
        def is_me(m):
            return m.author == self.bot.user

        # This works for now... Want to make it so it doesnt get rate limited / look suspicious...
        # deleted = await channel.purge(limit=amount, check=is_me)
        history = await channel.history(limit=amount).flatten()
        print(history)
        # await ctx.send('Deleted {} message(s)'.format(len(deleted)))