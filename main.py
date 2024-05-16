from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message
import asyncio
from responses import get_response
import requests
import json

#LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# HANDLING STARTUP FOR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    # if the message is coming from our user
    if message.author == client.user:
        return
    #---------------------------------------------------------------------------------
    user_message = message.content[9:].strip().lower()

    if user_message.startswith('clear'):
        await clear_messages(message, user_message)
    elif user_message.startswith('help'):
        await help_messages(message)
    elif user_message.startswith('meme'):
        await meme_messages(message)
    elif user_message.startswith('ping'):
        # Calculate the bot's latency
        latency = round(client.latency * 1000)  # Convert to milliseconds and round
        # Send a message with the bot's latency
        await message.channel.send(f'Pong! Latency: {latency}ms')
    else:
        await send_messages(message)

# CLEAR FUNCTION

async def clear_messages(message: Message, user_message: str) -> None:
    # Check if the user has permission to manage messages
    if message.author.guild_permissions.manage_messages:
        try:
            # Get the number of messages to delete
            num_to_delete = int(user_message.split(' ')[1]) + 1  # Add 1 to include the !clear message itself

            # Delete messages
            await message.channel.purge(limit=num_to_delete)
            cleared_messages = await message.channel.send(f"{num_to_delete - 1} messages cleared.")
            # Delete the confirmation message after 5 seconds (adjust as needed)
            await asyncio.sleep(5)
            await cleared_messages.delete()
        except IndexError:
            await message.channel.send("Please specify the number of messages to clear. !sakebot clear <number>")
        except ValueError:
            await message.channel.send("Invalid number of messages specified.")
    else:
        await message.channel.send("You don't have permission to clear messages.")
    #---------------------------------------------------------------------------------

# MESSAGE FUNCTIONALITY
async def send_messages(message: Message) -> None:
    if message.content.startswith('!sakebot'):
        if message.author.guild_permissions.manage_messages:
            try:
                await message.channel.send(f"Please specify a command after !sakebot.")
            except IndexError:
                await message.channel.send(f'Invali command. Please use "!sakebot help" for a list of commands.')
            except ValueError:
                await message.channel.send(f'Invali command. Please use "!sakebot help" for a list of commands.')
    else:
        pass

# HELP COMAMND FUNCTIONALITY
async def help_messages(message: Message) -> None:
    if message.author.guild_permissions.manage_messages:
        await message.channel.send(f'COMMANDS: help | clear | ping | meme')

# MEME FUNCTION
async def meme_messages(message: Message):
    content = requests.get("https://meme-api.com/gimme").text
    data = json.loads(content)
    embed = discord.Embed(title=f"{data['title']}", color=discord.Colour.random()).set_image(url=f"{data['url']}")
    await message.channel.send(embed=embed)

# MAIN ENTRY POINT FOR THE BOT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()