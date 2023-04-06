import aiohttp
import asyncio
import discord
import io
import logging
import json
import urllib.request
import string
from random import choice
import parser


from redbot.core import commands
from redbot.core.commands import Cog

class femboyYTs(Cog):
    """
    Get a random video from a Youtube Channel
    """
    def __init__(self, bot: Red) -> None:
        super().__init__()
        self.__session = aiohttp.ClientSession()
        self.bot = bot
    
    def cog_unload(self) -> None:
        if self.__session:
            asyncio.get_event_loop().create_task(self.__session.close())

    __author__ = ["sw1p3d"]
    __version__ = ".1"

    @commands.command()
    async def Linechu(self, ctx: commands.Context) -> None:
        """Gets a random Linechu video"""

        count = 50
        API_KEY = 'AIzaSyCkMbehTBfe-2yQ2mGzFvQq21zG1yra5vI'

        urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q=Linechu"
        # Get channel url
        channel_url = feedparser.parse("https://www.youtube.com/feeds/videos.xml?user=linechu")

        # Grab random video
        video = choice(channel_url.entries)
        
        await ctx.send(video)
