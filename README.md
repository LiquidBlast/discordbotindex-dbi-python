## Discord Bot Index API Wrapper 🎉
API Wrapper for [Discord Bot Index](https://discordbotindex.com) [DBI]

This project is made for **Python**!

### What does this wrapper do?
- Posts bot `GUILD_COUNT` to DBI.
- Fetches bot information/stats

### How do I use this?

> Run this command in your console:
```
pip install dbipyt
```

> To post your bot's guild count:
```
from dbipyt import post

await dbipyt.post(token="your-token-here", guild_count=len(bot.guilds))
```

> To fetch bot information:
```
from dbipyt import fetch

r = await dbipyt.fetch(bot_id="bot-id-here")
print(r) # This will print out the JSON response. Ex. r['prefix'] will return the bot's prefix
```


