from Controllers.twitterApiController import TwitterApi
from Controllers.bddController import dataBase
from dataModel.subTweet import SubTweetObject
from dataModel.tweeterUser import TweeterUser
from dataModel.tweet import TweetObj

class Engine:

    def __init__(self):
        self.bdd = dataBase()
        self.twp = TwitterApi()



    def register(self, param=None) -> str: # param = string de username/@username
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

    def getUserNameById(self, id: int = 0) -> str:
        user = self.twp.userRequestById(id)['data']
        return(user['username'])

    def scrapTweets(self):
        users = self.bdd.getUserData()

        for u in users:
            usr = TweeterUser(u['id'], desc=u['description'], name=u['user'], created_at=u['created_at'], username=u['username'])
            tweets = self.twp.tweetsRequest(usr.getId())
            for t in tweets['data']:
                try:
                    twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'], referenced_tweets=t['referenced_tweets'][0]['id'], author_id=t['author_id'])
                except:
                    twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'], author_id=t['author_id'])

                if self.bdd.searchData(twt) == False:
                    self.bdd.appendData(twt)
        return

    def pullTweets(self):
        return(self.bdd.getTweetData())

    def pullSubTweet(self, id) -> SubTweetObject:
        tmpTweet = SubTweetObject(id)

        if self.bdd.searchData(tmpTweet) == True:
            tmpTweet = self.bdd.getTweetData(tmpTweet)
        else: # search in bdd == False
 #           try:
    
            t = self.twp.subTweetsRequest(id)
            try:
                t = t['data'][0]
            except:
                return(SubTweetObject(0, text="Le tweet n'éxiste plus !"))
            tmpTweet = SubTweetObject(t['id'], t['text'], t['created_at'], 0)
            self.bdd.appendData(tmpTweet)
#            except:
#                tmpTweet = SubTweetObject(0, text="Le tweet n'éxiste plus !",)
        return(tmpTweet)

    
    def validateTweet(self, tweet):
        self.bdd.updateData(TweetObj(tweet['id'], text=tweet['text'], created_at=tweet['created_at'], pushed=1, author_id=tweet['author_id']))
        return