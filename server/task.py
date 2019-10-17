import os
import discord
from celery import Celery
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


# TODO: Put these in config possibly.
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Create celery broker with redis backend and update
celery = Celery('ghost-task', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
celery.conf.update(BROKER_URL=CELERY_BROKER_URL, CELERY_RESULT_BACKEND=CELERY_RESULT_BACKEND)

# Task to just test that tasks are working
@celery.task
def hello(msg):
    return "Hello. Here is your msg: " + msg

# Celery task to return the user name
@celery.task
def get_discord_user():
    print(client.user)
    return client.user