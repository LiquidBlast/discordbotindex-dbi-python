import aiohttp
import json

class Client:
    def __init__(self, token):
        self.auth = token

    async def post(self, bot_id:str=None, guild_count:int=None):
        async with aiohttp.ClientSession(headers={'Authorization': self.auth}) as s:
            async with s.post(f"https://discordbotindex.com/apiv1/bot/{bot_id}", data={'server_count': guild_count}) as r:
                r = await r.json()
                return r

#class Fetch:
async def fetch(bot_id, endpoint:str=None):
    async with aiohttp.ClientSession() as s:
        async with s.get(f"https://discordbotindex.com/apiv1/bot/{bot_id}") as r:
            r = await r.json()
            if endpoint is None:
                try:
                    return r
                except:
                    return "[dbipyt.0.1.1] Invalid client ID. Please provide a client ID with the bot_id argument."
            else:
                try:
                    return r[endpoint]
                except KeyError as e:
                    return f"[dbipyt.0.1.1] Invalid endpoint: {e}"
