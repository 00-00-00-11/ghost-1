from cogs.Moderation import Moderation
from cogs.Testing import Testing
from cogs.UserInfo import UserInfo
from cogs.Random import Random
from cogs.ServerInfo import ServerInfo
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

# Cogs import

# Get important data from the env file.
OWNER_ID = os.getenv('OWNER_ID')
USER_TOKEN = os.getenv('USER_TOKEN')
PREFIX = os.getenv('PREFIX')

class Selfbot(object):
    def __init__(self, token, owner_id, prefix=','):
        self.token = token
        self.prefix = PREFIX
        self.owner_id = owner_id
        self.client = commands.Bot(command_prefix=self.prefix, help_command=None,
                                   description=None, self_bot=True, owner_id=self.owner_id)
        self.register_cogs()
    
    def register_cogs(self):
        self.client.add_cog(ServerInfo(self.client))
        self.client.add_cog(Random(self.client))
        self.client.add_cog(UserInfo(self.client))
        self.client.add_cog(Testing(self.client))
        self.client.add_cog(Moderation(self.client))
    
    def run(self):
        self.client.run(self.token, bot=False)
    
    # @self.client.event
    # async def on_ready():
    #     print(f'Logged in as {client.user}')


bot = Selfbot(USER_TOKEN, OWNER_ID, PREFIX)
bot.run()