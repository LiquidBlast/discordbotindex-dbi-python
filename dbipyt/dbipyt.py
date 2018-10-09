import aiohttp

class dbipyt:
    def __init__(self):

    async def post(self, token, bot_id, guild_count):
        async with aiohttp.ClientSession(headers={'Authorization': token}) as s:
            async with s.post(f"https://discordbotindex.com/apiv1/bot/{bot_id}", data={'server_count': guild_count}) as r:
                r = await r.json()
                return r

    async def fetch(self, bot_id):
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://discordbotindex.com/apiv1/bot/{bot_id}") as r:
                r = await r.json()
                return r
