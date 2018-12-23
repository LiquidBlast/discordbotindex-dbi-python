import aiohttp
from .errors import InvalidEndpoint, InvalidToken, InvalidClientID

class Client:
    def __init__(self, token):
        self.auth = token

    async def post(self, bot_id:str=None, guild_count:int=None):
        async with aiohttp.ClientSession(headers={'Authorization': 'e'}) as s:
            async with s.post(f"https://discordbotindex.com/apiv1/bot/{bot_id}", data={'server_count': guild_count}) as r:
                r = await r.json()
                if r == {"error": "unauthorized"}:
                    raise InvalidToken("You provided an invalid token.")
                else:
                    return r

async def fetch(bot_id, endpoint:str=None):
    async with aiohttp.ClientSession() as s:
        async with s.get(f"https://discordbotindex.com/apiv1/bot/{bot_id}") as r:
            r = await r.json()
            if r == {"error":"unknown_bot"}:
                raise InvalidClientID(f"'{bot_id}' is not a valid ID. Please provide a correct client ID.")
            elif r == {"error":"param_must_be_int"}:
                raise InvalidClientID("Client IDs must be in int.")
            elif endpoint is None:
                return r
            else:
                try:
                    return r[endpoint]
                except KeyError as error:
                    raise InvalidEndpoint(error)
