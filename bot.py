import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("TOKEN")

TOKEN = "YOUR_TOKEN_HERE"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
