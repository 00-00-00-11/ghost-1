import discord
from discord.ext import commands
from utils.pastebin import pastebin
import aiohttp
import asyncio


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        """Get server info."""
        await ctx.message.delete()

        server = ctx.message.guild

        online = 0
        for i in server.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1

        all_users = []
        for user in server.members:
            all_users.append('{0}#{1} ({2} {3})'.format(
                user.name, user.discriminator, user.id, user.created_at.__format__(
                    '%A, %B %d %Y @ %H:%M:%S')))
        all_users.sort()
        all = '\n'.join(all_users)

        channel_count = len(
            [x for x in server.channels if type(x) == discord.channel.TextChannel])

        role_count = len(server.roles)
        emoji_count = len(server.emojis)

        url = await pastebin(str(all))
        hastebin_of_users = '[List of all {} users in this server]({})'.format(
            server.member_count, url)

        jsonData = {
            "title": 'Server Info: {0}'.format(server.name),
            # TODO: Pass the actual date-time through.
            "icon_url": str(server.icon_url),
            "owner": str(server.owner),
            "members": server.member_count,
            "currently_online": online,
            "text_channels": str(channel_count),
            "region": server.region,
            "verification_level": str(server.verification_level),
            "number_of_roles": str(role_count),
            "number_of_emotes": str(emoji_count),
            "hastebin_of_users": hastebin_of_users,
            "created_at": server.created_at.__format__(
                '%A, %B %d %Y @ %H:%M:%S')
        }
        
        async with aiohttp.ClientSession() as session:
            await session.post('http://localhost:3000/serverinfo', json=jsonData)

    @commands.command()
    async def userdump(self, ctx):
        """Get a list of all the users in the current server."""
        await ctx.message.delete()

        server = ctx.message.guild

        all_users = []
        for user in server.members:
            all_users.append('{0}#{1} ({2}) {3}'.format(
                user.name, user.discriminator, user.id, user.created_at.__format__(
                    '%A, %B %d %Y @ %H:%M:%S')))
        all_users.sort()
        users = '\n'.join(all_users)
        url = await pastebin(str(users))

        jsonData = {
            "title": 'User List - {} members'.format(server.member_count),
            "description": url,
            "footer": 'Server ID: {}'.format(server.id)
        }

        async with aiohttp.ClientSession() as session:
            await session.post('http://localhost:3000/userdump', json=jsonData)
