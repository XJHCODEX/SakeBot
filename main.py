from typing import Final
import os
import discord
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# MESSAGE FUNCTIONALITY

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    
    if user_message.startswith('!SakeBot'):
        user_message = user_message[9:].strip# Removes "!SakeBot" from the message

    """
    if is_private:= user_message[0] == '?':
        user_message = user_message[1:]
    """
    try:
        response: str = get_response(user_message)
        # if message is private we send it to the author
        # otherwise we send it to the current channel
        # must await message.author.send and message.channel.send
        await message.author.send(response) # if is_private else await message.channel.send(response)
        # - change exception handling -
    except discord.Forbidden:
        return
    except Exception as e:
        print(e)

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
    elif user_message.startswith('!sakebot'):
        await send_message(message, "I'm not sure what you mean by that.")
    else:
        await send_message(message, "Command not recognized.")

async def clear_messages(message: Message, user_message: str) -> None:
    # Check if the user has permission to manage messages
    if message.author.guild_permissions.manage_messages:
        try:
            # Get the number of messages to delete
            num_to_delete = int(user_message.split(' ')[1]) + 1  # Add 1 to include the !clear message itself

            # Delete messages
            await message.channel.purge(limit=num_to_delete)
            await message.channel.send(f"{num_to_delete - 1} messages cleared.")
        except IndexError:
            await message.channel.send("Please specify the number of messages to clear. !sakebot clear <number>")
        except ValueError:
            await message.channel.send("Invalid number of messages specified.")
    else:
        await message.channel.send("You don't have permission to clear messages.")
    #---------------------------------------------------------------------------------
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    # channel the message is coming from - user who sent the message - user message
    print(f'[{channel}] {username}: "{user_message}"')

    # we want to send the message
    await send_message(message, user_message)

# MAIN ENTRY POINT FOR THE BOT
def main() -> None:
    client.run(token=TOKEN)

if __name__ == "__main__":
    main()