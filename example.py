import discord
from discord.ext import commands
from dbipyt import dbipyt

bot = commands.Bot(command_prefix='!')

@bot.command()
@commands.is_owner()
async def post(ctx):
    
    client = dbipyt.Client(token='token')
    r = await client.post(bot_id='id', guild_count=len(bot.guilds))
    await ctx.send(f"Posted! Reponse: {r}")
    
@bot.command()
async def botinfo(ctx, bot_id):
    
    # to get the whole JSON response..
    r = await dbipyt.fetch(bot_id='id')
    await ctx.send(f"Prefix: {r['prefix']}, Description: {r['shortdesc']}, Upvotes: {r['upvotes']}")
                   
    # to get each endpoint..
    prefix = await dbipyt.fetch(bot_id='id', endpoint='prefix') # endpoints: https://discordbotindex.com/documentation
    short_description = await dbipyt.fetch(bot_id='id', endpoint='shortdesc')
    upvotes = await dbipyt.fetch(bot_id='id', endpoint='upvotes')
    await ctx.send(f"Prefix: {prefix}, Description: {shortdesc}, Upvotes: {upvotes}")
    
                  


bot.run('token')
