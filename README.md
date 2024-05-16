# Discord Bot - SakeBot

SakeBot is a Discord bot designed to provide various commands and functionalities to users in a Discord server.

## Getting Started

To use SakeBot in your Discord server, follow these steps:

1. **Invite the Bot to Your Server**:
   - Use the following invite link to add SakeBot to your Discord server:
     [Invite SakeBot](https://www.discord.com/oauth2/authorize?client_id=1239268194808631419&permissions=1248256&scope=bot)
   - Replace `YOUR_CLIENT_ID` with your bot's client ID.
   - Customize the `YOUR_PERMISSIONS` field with the necessary permissions for your bot (e.g., read messages, send messages, manage messages, etc.).

2. **Configure Environment Variables**:
   - Create a `.env` file in the root directory of your bot project.
   - Add your Discord bot token to the `.env` file using the following format:
     ```
     DISCORD_TOKEN=your_bot_token_here
     ```

3. **Run the Bot**:
   - Install the required Python packages using `pip install -r requirements.txt`.
   - Install discord bot package `pip install discord`.
   - Install python-dotenv to have a place for our discord token `pip install python-dotenv`.
   - Run the bot using `python main.py`.
   - Include giving particular commands to the BOT.

### General Commands

- `!sakebot help`: List available commands. (work in progress)
- `!sakebot clear <num_messages>`: Clear messages in the current channel.
- `!sakebot ping`: Pings bot.
- `!sakebot meme`: Sends a meme.

### Bot Response

- When you mention or address the bot without a recognized command, it responds with "I'm not sure what you mean by that."

### Additional Functionality

- The bot automatically converts all incoming messages to lowercase for case-insensitive command processing.
- It provides error handling for invalid commands and user inputs.

## Contributing

If you'd like to contribute to SakeBot, feel free to fork the repository and submit pull requests with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
