import discord
from discord.ext import commands
from discussion import discussion_events


# initialisation du BOT
intents = discord.Intents.all()
# permet au bot d'accéder aux informations des membres du serveur.
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = ''

# fonctions qui nous sert pour initier tout les evenements lié a la discussion avec le BOT
discussion_events(bot)

# run le bot
bot.run(TOKEN)