import discord
from discord.ext import commands
from shared import ignored_commands, user_histories
from command import register_events

# initialisation du BOT
intents = discord.Intents.all()
# permet au bot d'accéder aux informations des membres du serveur.
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = ''

# fonctions qui nous sert pour initier tout les evenements lié a l'historique
register_events(bot)

# run le bot
bot.run(TOKEN)
