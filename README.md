# Discord Moderation Bot

Enhance your Discord server with advanced moderation tools.

## Features

- Warning system with SQLite database
- AutoMod integration for automatic message filtering
- Configurable warning thresholds
- Warning roles and expiration
- Case system and notes
- Appeal system

## Requirements

- Python 3.6 or higher
- discord.py
- Flask
- sqlite3
- python-dotenv

## Installation

1. Clone the repository:

```bash

git clone https://github.com/EnderDevelopment/discord-moderation-bot.git

cd discord-moderation-bot

```

2. Install the required packages:

```bash

pip install -r requirements.txt

```

3. Create a `.env` file in the root directory and add your Discord bot token:

```env

DISCORD_TOKEN=your_discord_bot_token

```

## Usage

1. Start the bot:

```bash

python bot.py

```

2. Access the dashboard at `http://localhost:5000` to configure the bot.

## Commands

| Command | Description | Permissions |
|---------|-------------|-------------|
| !warn <member> <reason> | Warn a member | Moderator |
| !warnings <member> | View a member's warnings | Moderator |
| !dashboard | Get the dashboard URL | Moderator |

## Configuration

Configure the bot by accessing the dashboard at `http://localhost:5000`. You can set the warning threshold and other moderation settings.

---

## Generated with EnderDevelopment

This plugin was generated in minutes with [EnderDevelopment](https://enderdevelopment.com) — the AI platform that turns your ideas into working Minecraft plugins, Discord bots and FiveM scripts.

**Want your own?** [Generate this project on EnderDevelopment](https://dash.enderdevelopment.com?utm_source=github&utm_medium=readme&utm_campaign=discord-moderation-bot&utm_content=bottom) — describe it in one sentence and get the full source code.
