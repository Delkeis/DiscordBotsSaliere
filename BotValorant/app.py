import discord
from Config import *
from GameApp.gameApp.GameApp import GameApp
from GameApp.gameApp.Config.ConfigMod import ConfigMod
from Function.IncludedFunction import *

#Classe My Client qui hérite de Discord.client
# https://discordpy.readthedocs.io/en/stable/api.html#client
# elle permet d'interagir avec discrod et ses interaction
# !!!!!! overload une fonction détruit la fonction parent !!!!!!!
class MyClient(discord.Client):
    #   définition
    #
    #   Gapp : classe contiens toutes les composante de jeux /bdd /scrapping d'info 
    #
    Gapp = GameApp()
    Gapp.start()

    # on_ready est appeler juste quand le bot est actif !
    async def on_ready(self):
        print("bot logged in as")
        print(self.user.name)
        print("------")
        chan = client.get_channel(int(ConfigMod().getParameter("channelId", section="DiscordInfo")))
        appname = ConfigMod().getParameter("BotName", section="BotInfo")
        await chan.send("Bonjour je suis connecter en tant que "+appname+", hello !")

    # on_message est appeler quen un utilisateur envoie un message sur n'importe quel channel du discord!
    async def on_message(self, message):
        #print(message.content.startswith())
        #match message.content:
        #    case startswith("!start"):
        #        print("works-----------")

        if message.author.id == self.user.id:
            return
        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif message.content.startswith('!getuid'):
            myCommand = message.content.replace('!getuid ', '')
            await message.reply('Your Riot Puuid is : '+str(self.Gapp.newComm(myCommand)), mention_author=True)
        elif message.content.startswith('!register'):
            myCommand = message.content.replace('!register ', '')
            self.Gapp.register(myCommand)
        elif message.content.startswith('!help'):
            await message.channel.send("Commandes :\n\t- !getuid     {pour avoir sun Puuid riot game}\n\t- !register RiotId#Tag     {pour s'inscrire dans la base de donnée}")
        elif message.content.startswith('!quit'):
            await message.channel.send("Bye !")
            await self.loop.close()



# on initialise le bot 
client = MyClient()
# on lance le bot avec le fichier de config 
# la variable my_config est contenu dans Config.py 
client.run(ConfigMod().getParameter("discordToken"))# my_config["DISCORD_TOKEN"])
