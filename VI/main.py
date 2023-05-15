import discord
from discord.ext import commands
from googletrans import Translator
from translate import Translate


intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = 'MTA5MTMzNDE2MDk1NTc0ODQyMg.GJmPLv.F6a8usXf6oIOV3threVGNZMdd0ncIMnKMbbFNw'


Translate(bot)


bot.run(TOKEN)
