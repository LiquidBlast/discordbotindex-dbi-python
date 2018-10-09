import aiohttp

class dbipyt:

    async def post(token, bot_id, guild_count):
        async with aiohttp.ClientSession(headers={'Authorization': token}) as s:
            async with s.post(f"https://discordbotindex.com/apiv1/bot/{bot_id}", data={'server_count': guild_count}) as r:
                r = await r.json()
                return r

    async def fetch(bot_id):
        async with aiohttp.ClientSession() as s:
            async with s.get(f"https://discordbotindex.com/apiv1/bot/{bot_id}") as r:
                r = await r.json()
                return r
