import aiohttp
import os
from pbwrap import Pastebin
from dotenv import load_dotenv
load_dotenv()

PASTEBIN_API_KEY = os.getenv('PASTEBIN_API_KEY')


async def pastebin(content):
    pastebin = Pastebin(api_dev_key=PASTEBIN_API_KEY)

    link = pastebin.create_paste(api_paste_code=content, api_paste_private=1)
    return link