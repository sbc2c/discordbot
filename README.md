# Discord Blackjack Bot

A simple Discord bot that lets users play Blackjack using commands like !blackjack, !hit, and !stand.

---

## Features

- Start a blackjack game with !blackjack
- Draw cards with !hit
- End turn with !stand
- Dealer plays automatically
- Win / lose / tie system

---

## Requirements

- Discord bot token
- Discord server where you can add bots

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

---

### 2. Create virtual environment (recommended)

python3 -m venv venv
source venv/bin/activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Create a .env file

Create a file named .env in the project folder.

Add this inside:

TOKEN=your_discord_bot_token_here

---

### 5. Enable Discord intents

Go to:
https://discord.com/developers/applications

Then:
- Select your bot
- Go to Bot tab
- Enable MESSAGE CONTENT INTENT
- Save changes

---

### 6. Invite bot to your server

Use this link:

https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&scope=bot&permissions=68608

Replace YOUR_CLIENT_ID with your Application ID.

---

## Run the bot

python bot.py

If successful, you should see:

Logged in as <bot name>

---

## Commands

!blackjack - Start a game
!hit - Draw a card
!stand - End turn

---

## Notes

- Never share your bot token
- Keep .env in .gitignore
- Bot must be running for commands to work

---

## Troubleshooting

Bot not responding:
- Check MESSAGE CONTENT INTENT is enabled
- Make sure bot is online

Token errors:
- Check .env format:
TOKEN=your_token_here
