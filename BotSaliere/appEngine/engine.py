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

    def scrapTweets(self):
        users = self.bdd.getUserData()

        for u in users:
            usr = TweeterUser(u['id'], desc=u['description'], name=u['user'], created_at=u['created_at'], username=u['username'])
            tweets = self.twp.tweetsRequest(usr.getId())
            for t in tweets['data']:
                twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'])
                if self.bdd.searchData(twt) == False:
                    self.bdd.appendData(twt)
        return

    def putTweets(self):
        return(self.bdd.getTweetData())
    
    def validateTweet(self, tweet):
        self.bdd.updateData(TweetObj(tweet['id'], text=tweet['text'], created_at=tweet['created_at'], pushed=1))
        return