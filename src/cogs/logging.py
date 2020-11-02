import discord
from discord.ext import commands


class Logging(commands.Cog):
  """
  A cog with a listener that logs a little information about each message.
  The listener explicitly excludes messages from the bot itself.
  """

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message: discord.Message):
    if message.author == self.bot.user: return
    length = len(message.content)
    print(f'Message from {message.author} is {length} bytes long!')

 
def setup(bot: commands.Bot):
  print('Setting up logging...')
  cog = Logging(bot)
  bot.add_cog(cog)
