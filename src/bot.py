import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

# Get important data from the env file.
OWNER_ID = os.getenv('OWNER_ID')
BOT_TOKEN = os.getenv('BOT_TOKEN')
PREFIX = os.getenv('PREFIX')

# Create bot with settings from .env
client = commands.Bot(command_prefix=PREFIX, help_command=None,
                      description=None, self_bot=False, owner_id=OWNER_ID)


# Runs when the on_ready client event is sent
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


@client.command()
async def test(ctx):
    await ctx.send('hey there!')

# Run 'Ghost Assistant' bot
client.run(BOT_TOKEN, bot=True)