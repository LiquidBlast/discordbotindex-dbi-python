## Python Discord Bot Index API Wrapper 🎉
API Wrapper for [Discord Bot Index](https://discordbotindex.com)

Version: **0.0.1**

### What does this wrapper do?
- Posts bot `GUILD_COUNT` to DBI.
- Fetches bot information/stats

### How do I use this?

> Run this command in your console:
```
pip3 install dbipyt
```

> To post your bot's guild count:
```
from dbipyt import dbipyt

await dbipyt.dbipyt.post(token="your-token-here", bot_id="bot-id-here", guild_count=len(bot.guilds))
```

> To fetch bot information:
```
from dbipyt import dbipyt

r = await dbipyt.dbipyt.fetch(bot_id="bot-id-here")
print(r) # This will print out the JSON response. Ex. r['prefix'] will return the bot's prefix
```


For questions and concerns, submit an issue, or contact me on Discord: `lukee#0420`
