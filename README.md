## Python Discord Bot Index API Wrapper 🎉
API Wrapper for [Discord Bot Index](https://discordbotindex.com)

Current Version: **0.1.2**

### What does this wrapper do?
- Posts bot `GUILD_COUNT` to DBI.
- Fetches bot information/stats

### How do I use this?

> Run this command in your console:
```sh
$ pip3 install dbipyt
```

> To post your bot's guild count:
```py
from dbipyt import dbipyt
client = dbipyt.Client(token='token')
p = await client.post(bot_id='id', guild_count=len(bot.guilds))
print(p)
```

> To fetch bot information:
```py
from dbipyt import dbipyt
p = await dbipyt.fetch(bot_id='id', endpoint='endpoint') # if you wish to get the JSON response, do not add the endpoint argument
print(p)
```

For questions and concerns, submit an issue, or contact me on Discord: `lukee#0420`
