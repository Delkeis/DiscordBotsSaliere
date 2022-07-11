from Controllers.twitterApiController import TwitterApi
from appEngine.engine import Engine
from PyInclude import *
from discord.ext import tasks

################################################
#
#
################################################
class MyClient(discord.Client):
    en = Engine()

    async def on_ready(self):
        print("bot logged in as")
        print(self.user.name)
        print("------")
        self.chan = client.get_channel(int(ConfigMod().getParameter("channelId", section="DiscordInfo")))
        appname = ConfigMod().getParameter("BotName", section="BotInfo")
        await self.chan.send("Bonjour je suis connecter en tant que "+appname+", hello !")
        self.mytask.start()




    @tasks.loop(seconds=30)
    async def mytask(self):

        self.en.scrapTweets()
        twt = self.en.pullTweets()
        for t in twt:
            if t['pushed'] == 0:
                usrName = self.en.getUserNameById(id=int(t['author_id']))
                uri = "https://twitter.com/{}/status/{}".format(usrName, t['id'])
                mess = "Tweet from {} :".format(usrName)
                await self.chan.send(mess)
                await self.chan.send(uri)
                self.en.validateTweet(t)





    async def on_message(self, message):
        #print(message.content.startswith())
        #match message.content:
        #    case startswith("!start"):
        #        print("works-----------")

        if message.author.id == self.user.id:
            return
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

client = MyClient()
client.run(ConfigMod().getParameter("discordToken"))# my_config["DISCORD_TOKEN"])
