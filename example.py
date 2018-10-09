import discord
from discord.ext import commands
from dbipyt import fetch, post

bot = commands.Bot(command_prefix='!')

@bot.command()
@commands.is_owner()
async def post(ctx):
    r = await dbipyt.post(token="your-token-here", guild_count=len(bot.guilds))
    await ctx.send(f"Posted! Reponse: {r}")
    
@bot.command()
async def botinfo(ctx, bot_id):
    r = await dbipyt.fetch(bot_id=bot_id)
    await ctx.send(f"Prefix: {r['prefix']}, Description: {r['shortdesc']}, Upvotes: {r['upvotes']}")


bot.run('token')
