#imports
import discord
from discord.ext import commands

# Creds
TOKEN = 'OTU4ODcyNzM1NjAwMjQyNjg4.YkTp0w.W73uhl6Zm0wVFqaZNjYoRF64I3Y'

#create bot
client = commands.Bot(command_prefix = '!')

#startup Info
@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

#command
@client.command()
async def helloworld(ctx):
    await ctx.send('Hello World!')

#run the bot
client.run(TOKEN)

