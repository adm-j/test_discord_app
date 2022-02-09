import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event   # When a user dms the bot or messages in the channel, greets the user
async def on_message(message):
    await message.author.send(f'hello {message.author}')


client.run(TOKEN)
