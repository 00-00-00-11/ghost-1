import discord
from discord.ext import commands
import asyncio
import aiohttp


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, user: discord.User):
        """Get user info."""

        await asyncio.sleep(0.5)
        await ctx.message.delete()

        if user == ctx.message.author:
            is_friend = 'N/A'
            is_blocked = 'N/A'
        else:
            is_friend = user.is_friend()
            if is_friend == True:
                is_blocked = None
            else:
                is_blocked = user.is_blocked()

        jsonData = {
            "title": 'User Info for {}'.format(user.name),
            "thumbnail": str(user.avatar_url),
            "id": user.id,
            "is_friend": is_friend,
            "is_blocked": is_blocked,
            "created_at": user.created_at.__format__('%A, %B %d %Y @ %H:%M:%S')
        }

        async with aiohttp.ClientSession() as session:
            await session.post('http://localhost:3000/userinfo', json=jsonData)
