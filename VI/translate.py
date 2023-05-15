from googletrans import Translator
translator = Translator()

def Translate(bot):
    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.command()
    async def translate(ctx, lang, *, text):
        translation = translator.translate(text, dest=lang)
        await ctx.send(f'Translated text: {translation.text}')