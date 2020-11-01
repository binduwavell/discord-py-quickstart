import discord
from discord.ext import commands


class Utilities(commands.Cog):
  """
  A cog that registers the ping command.
  """

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.command()
  async def ping(self, message: discord.Message):
    """You say ?ping and the bot will reply Pong!"""
    await message.channel.send('Pong!')


def setup(bot: commands.Bot):
  print('Setting up utilities...')
  cog = Utilities(bot)
  bot.add_cog(cog)