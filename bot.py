import discord
from discord.ext import commands


from module1 import CommandHistory


# Création des intents pour le bot
intents = discord.Intents.all()
intents.members = True
user_histories = {}

# Création de l'objet bot avec le préfixe de commande et les intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Création d'instances des modules personnalisés pour le bot
bot.history = CommandHistory()


ignored_commands = ["!lastcmd", "!forward", "!back", "!history", "!clear_history"]


# Définition d'un événement pour quand le bot est prêt
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")
    # await send_motivation_quote() #teste de l'envoi de la citation

# Définition d'une commande pour supprimer les messages en masse(limitation à 10)
@bot.command(name="del")
async def delete(ctx):
    await ctx.channel.purge(limit=10)

# Commande servant de test
@bot.command(name="focus")
async def focus(ctx):
    await ctx.send("Restez concentré")


@bot.event
async def on_command_completion(ctx):
    if ctx.message.content not in ignored_commands:
        bot.history.add_command(ctx.message.content)

# Commande pour afficher l'historique des commandes
@bot.command(name="history")
async def history(ctx):
    commands = bot.history.get_all_commands()
    if commands == "Pas d'historique":
        await ctx.send("Aucune commande dans l'historique.")
    else:
        commands_str = "\n".join(commands)
        await ctx.send(f"Historiques des commandes :\n```{commands_str}```")

# Commande pour afficher la dernière commande
@bot.command(name="lastcmd")
async def last_command(ctx):
    last_cmd = bot.history.get_last_command()
    if last_cmd == "Pas d'historique":
        await ctx.send("Aucune commande dans l'historique.")
    else:
        await ctx.send(f"Dernière commande : {last_cmd}")

# Commande pour revenir en arrière dans l'historique des commandes
@bot.command(name="back")
async def back(ctx):
    command = bot.history.move_backward()
    if command:
        await ctx.send(f"Dernière commande : {command}")
    else:
        await ctx.send("Début de l'historique atteint.")

# Commande pour avancer dans l'historique des commandes
@bot.command(name="forward")
async def forward(ctx):
    command = bot.history.move_forward()
    if command:
        await ctx.send(f"Dernière commande : {command}")
    else:
        await ctx.send("Fin de l'historique atteint.")

# Commande pour effacer l'historique des commandes
@bot.command(name="clear_history")
async def clear_history(ctx):
    bot.history.clear()
    await ctx.send("L'historique a été supprimé.")

# Lancement du bot 
bot.run("code")

######################################################

@bot.event
async def on_command(ctx):
    user_id = ctx.author.id
    if user_id not in user_histories:
        user_histories[user_id] = CommandHistory()

    command_name = ctx.message.content.split()[0]
    if command_name not in ignored_commands:
        user_histories[user_id].add_command(ctx.message.content)

