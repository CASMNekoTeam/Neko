import discord

bot.event
async def on_ready():
     await client.change_presence(game=discord.Game(name='in development'),
                                 status=discord.Status('online'),
                                 afk=False)
    
    
bot.run('token')
