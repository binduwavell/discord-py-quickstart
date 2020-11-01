from cogs.logging import Logging
import discord
from discord.ext import commands
import importlib
import logging
import sys
from termcolor import colored


# Documentation
#   https://discordpy.readthedocs.io/en/latest/
#   https://github.com/binduwavell/discord-py-quickstart


# Load auth secrets if we have them or display help.
if importlib.util.find_spec('authsecrets'):
  import authsecrets
else:
  print(colored('ERROR: Missing authentication secrets.\n', 'red'))
  print(colored('Create a file named authsecrets.py in this directory.', 'green'))
  print(colored('This file should not be checked into source control.', 'green'))
  print(colored('The file contents should look like the following (with your actual token):\n', 'green'))
  print(colored('BOT_TOKEN="paste your bot token here"\n', 'white', attrs=['bold']))
  print(colored('See: https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro', 'green'))
  sys.exit(1)

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.members = True

EXTENSIONS = ['hotreload', 'logging', 'utilities']

bot = commands.Bot(command_prefix='?', help_command=commands.DefaultHelpCommand(), intents=intents)
[bot.load_extension(f'cogs.{ext}') for ext in EXTENSIONS]
bot.run(authsecrets.BOT_TOKEN)
