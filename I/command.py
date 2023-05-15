from shared import ignored_commands, user_histories
from I import History
# on importe le dictionnaire , les mots ignorés et surtout le fichier ou nos fonction d'events de commande pour l 'historique sont stockée

def register_events(bot):

    # on importe les functions et on les stocke dans bot.history
    bot.history = History()

    ##############################################################################
    # definition de tous les events avec les functions de la clas 'History' de I.py initié dans bot.history
    @bot.event
    async def on_ready():
        print(f"{bot.user.name} has connected to Discord!")

    @bot.command(name="del")
    async def delete(ctx):
        await ctx.channel.purge(limit=10)

    @bot.command(name="focus")
    async def focus(ctx):
        await ctx.send("Restez concentré")

    
    @bot.event
    async def on_command_completion(ctx):
        if ctx.message.content not in ignored_commands:
            bot.history.add(ctx.message.content)
    
    @bot.command(name="history")
    async def history(ctx):
        commands = bot.history.get_all_commands()
        if commands == "Pas d'historique":
            await ctx.send("Aucune commande dans l'historique.")
        else:
            commands_str = "\n".join(commands)
            await ctx.send(f"Historiques des commandes :\n```{commands_str}```")
    
    @bot.command(name="lastcmd")
    async def last_command(ctx):
        last_cmd = bot.history.get_last_command()
        if last_cmd == "Pas d'historique":
            await ctx.send("Aucune commande dans l'historique.")
        else:
            await ctx.send(f"Dernière commande : {last_cmd}")
    
    @bot.command(name="back")
    async def back(ctx):
        command = bot.history.move_backward()
        if command:
            await ctx.send(f"Dernière commande : {command}")
        else:
            await ctx.send("Début de l'historique atteint.")
    
    @bot.command(name="forward")
    async def forward(ctx):
        command = bot.history.move_forward()
        if command:
            await ctx.send(f"Dernière commande : {command}")
        else:
            await ctx.send("Fin de l'historique atteint.")
    
    @bot.command(name="clear_history")
    async def clear_history(ctx):
        bot.history.clear()
        await ctx.send("L'historique a été supprimé.")
    
    @bot.event
    async def on_command(ctx):
        user_id = ctx.author.id
        if user_id not in user_histories:
            user_histories[user_id] = History()
    
        command_name = ctx.message.content.split()[0]
        if command_name not in ignored_commands:
            user_histories[user_id].add(ctx.message.content)
