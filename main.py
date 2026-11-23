import discord
import os
import json
import random

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

parsed_lines = [];
with open("./public/json/cyn-string.json") as fd:
    parsed_lines = json.load(fd);


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("!"):
        return

    text = random.choice(parsed_lines)
    
    await message.channel.send(text)
    await bot.process_commands(message)

@bot.command()
async def enrique(ctx):
    await ctx.channel.send("ENRIQUE!!! :speaking_head: :speaking_head: :speaking_head:")

bot.run(TOKEN)