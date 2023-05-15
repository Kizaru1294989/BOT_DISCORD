import discord
from discord.ext import commands
from III import BinaryTreeNode
from III import BinaryTree
from arbre_binaire import question_tree, nginx_basic, nginx_advanced, apache_basic, apache_advanced



def discussion_events(bot):
 

    @bot.event
    async def on_ready():
        print(f"{bot.user.name} est connecté à Discord !")

    @bot.command(name="helps")
    async def helps(ctx):
        question = question_tree.get_current_question()
        await ctx.send(question)

    @bot.command(name="nginx")
    async def nginx(ctx):
        question_tree.traverse_left()
        question = question_tree.get_current_question()
        await ctx.send(question)

    @bot.command(name="apache")
    async def apache(ctx):
        question_tree.traverse_right()
        question = question_tree.get_current_question()
        await ctx.send(question)

    @bot.command(name="bases")
    async def bases(ctx):
        question_tree.traverse_left()
        answer = question_tree.get_current_question()
        await ctx.send(answer)

    @bot.command(name="advanced")
    async def advanced(ctx):
        question_tree.traverse_right()
        answer = question_tree.get_current_question()
        await ctx.send(answer)

    @bot.command(name="reset")
    async def reset(ctx):
        question_tree.reset()
        question = question_tree.get_current_question()
        await ctx.send("La conversation a été réinitialisée.")
        await ctx.send(question)


    @bot.command(name="oui")
    async def oui(ctx):
        if question_tree.current_node == nginx_basic:
            links = "Voici quelques liens pour apprendre les bases de nginx :\nNGINX: https://www.nginx.com/ "
        elif question_tree.current_node == nginx_advanced:
            links = "Voici quelques liens pour apprendre les concepts avancés de nginx :\nNGINX: https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/"
        elif question_tree.current_node == apache_basic:
            links = "Voici quelques liens pour apprendre les bases de apache :\nApache2: https://doc.ubuntu-fr.org/apache2 "
        elif question_tree.current_node == apache_advanced:
            links = "Voici quelques liens pour apprendre les concepts avancés de apache :\nApache2: https://httpd.apache.org/ "
        else:
            links = "Je ne peux pas vous donner de liens pour le moment."
        await ctx.send(links)
        await ctx.send("Bonne chance !")
        question_tree.reset()

    @bot.command(name="non")
    async def non(ctx):
        await ctx.send("Pas de Soucis")
        question_tree.reset()