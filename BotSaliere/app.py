from Controllers.twitterApiController import TwitterApi
from appEngine.engine import Engine
from PyInclude import *
from discord.ext import tasks

################################################
# My client est une class enfant de discord Client 
#   elle est le moteur du bot discord 
################################################
class MyClient(discord.Client):
    en = Engine()

    ########################################################
    #   la méthode on_ready est appeler au démarrage de la classe au même titre que __init__()
    #   on initialise le channel sur lequel parler et on lance la tâche asynchrone myTask()
    ########################################################
    async def on_ready(self):
        print("bot logged in as")
        print(self.user.name)
        print("------")
        self.chan = client.get_channel(int(ConfigMod().getParameter("channelId", section="DiscordInfo")))
        appname = ConfigMod().getParameter("BotName", section="BotInfo")
        await self.chan.send("Bonjour je suis connecter en tant que "+appname+", hello !")
        self.mytask.start()



    #########################################################
    #   la tâche myTask est une tâche asynchrone (qui est exécuter en permanance)
    #   qui consiste à récupérer les données et les envoyer sur le channel discord 
    #########################################################
    @tasks.loop(seconds=600)
    async def mytask(self):

        self.en.scrapTweets()
        twt = self.en.pullTweets()
        for t in twt:
            if t['pushed'] == 0:
                if t['type'] != 'tweeted':
                    id = t['referenced_tweets']
                else:
                    id = t['id']
                usrName = self.en.getUserNameById(id=int(t['author_id']))
                uri = "https://twitter.com/{}/status/{}".format(usrName, id)
                mess = "Tweet from {} :".format(usrName)
                await self.chan.send(mess)
                await self.chan.send(uri)
                self.en.validateTweet(t)




    ########################################################
    #   la méthode on_mesage est une méthode qui est appeler à chaque message sur le discord (tous les channels)
    #   on obtiens le contenu du message dans la variable message 
    ########################################################
    async def on_message(self, message):

        # je vérifie que le bot ne lise pas ses propre messages 
        if message.author.id == self.user.id:
            return

        
        # on vérifie grâce à startswith('') les mots clé entré par l'utilisateur
        if message.content.startswith('$hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
        elif message.content.startswith('$help'):
            with open("Config/help.txt") as f:
                helptxt = f.read()
            await message.channel.send(helptxt)
        elif message.content.startswith('$register'):
            myCommand = message.content.replace('$register ', '')
            rsp = self.en.register(myCommand)
            if rsp == False:
                rsp = "Erreur : L'utilisateur @{0} n'est pas trouvable !".format(myCommand)
            await message.channel.send(rsp)
        elif message.content.startswith('$sethashtag'):
            myCommand = message.content.replace('$sethashtag ', '')
            self.en.setHashTag(myCommand)
            await message.channel.send("le HashTag à été modifier par : {}".format(myCommand))
        elif message.content.startswith('$hashtag'):
            await message.channel.send("le hashTag est : {}".format(self.en.getHashTag()))


client = MyClient()
# client.run est hériter de discord.client et prend en paramètre le token de connexion
client.run(ConfigMod().getParameter("discordToken"))