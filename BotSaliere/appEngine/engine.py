import re
from Controllers.twitterApiController import TwitterApi
from Controllers.bddController import dataBase
from dataModel.tweet import TweetObj
from dataModel.tweeterUser import TweeterUser

class Engine:

    def __init__(self):
        self.bdd = dataBase()
        self.twp = TwitterApi()

    def register(self, param=None):
        if(param == None):
            return False

        if(str(param).startswith("@")):
            param = param.replace('@', '')

        if self.bdd.searchData(TweeterUser(0, username=param), userName=True) == False:
            req = self.twp.userRequest(param)
            try:
                usr = TweeterUser(req['data'][0]['id'], desc=req['data'][0]['description'], name=req['data'][0]['name'],
                                    created_at=req['data'][0]['created_at'], username=req['data'][0]['username'])
                self.bdd.appendData(usr)
            except:
                return False
            return("user : "+param+" à été ajouter à la base de donée")
        else:
            return("l'utilisateur existe déjà !")

    def buildRequest(self):
            
            rsp = self.twp.userRequest("NeoTastyNetwork")
            usr = TweeterUser(rsp['data'][0]['id'], desc=rsp['data'][0]['description'], name=rsp['data'][0]['name'],
                                created_at=rsp['data'][0]['created_at'], username=rsp['data'][0]['username'])
            print(rsp)
            if self.bdd.searchData(usr) == False:
                self.bdd.appendData(usr)
            tweets = self.twp.tweetsRequest(usr.getId())

            for t in tweets['data']:
                twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'])
                if self.bdd.searchData(twt) == False:
                    self.bdd.appendData(twt)
        
            print(tweets)