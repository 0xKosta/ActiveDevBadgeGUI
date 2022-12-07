import hikari
import lightbulb
import customtkinter

def main(token):
    bot = lightbulb.BotApp(token, banner=None)

    @bot.listen(lightbulb.LightbulbStartedEvent)
    async def started_event(event):
        print('''
==================================================================
     YOU CAN NOW USE THE COMMAND /BADGE IN THE DISCORD SERVER
==================================================================
        ''')

    @bot.command
    @lightbulb.command(name="badge", description="Run this command to be eligible for the Active Developer badge.")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def badge(ctx):
        print('''
===================================================================
                COMMAND HAS BEEN RECEIVED  
===================================================================    
        ''')
        embed = hikari.Embed(title="You did it!", description="When Discord refreshes command usage next, you will be able to claim your badge!")
        embed.set_author(name="Made by kosta#2202 @ github.com/buxx0")
        await ctx.respond(embed)
        print('''
===================================================================
  COMMAND HAS BEEN EXECUTED, YOU CAN SHUT OFF BOTH OF THE WINDOWS
===================================================================    
                ''')

    bot.run()
