from Controllers.twitterApiController import TwitterApi
from Controllers.bddController import dataBase
from dataModel.subTweet import SubTweetObject
from dataModel.tweeterUser import TweeterUser
from dataModel.tweet import TweetObj


#############################################
#   la classe engine est une classe dont le but est de regrouper toutes les action nésséssaire pour 
#   la récupération et le traitements des informations
#   elle fonctionne de concert avec les classes TwitterApi et dataBase
#############################################
class Engine:

    def __init__(self):
        self.bdd = dataBase()
        self.twp = TwitterApi()
        self.refresh__init__()
    
    def refresh__init__(self):
        self.modiese = self.bdd.get_setInfos()

    def setHashTag(self, hash:str):
        self.bdd.get_setInfos(set=True, nfo=hash)
        self.refresh__init__()
    
    def getHashTag(self) -> str:
        return self.modiese


    ###################################################
    #   la méthode register sert à enregistrer des utilisateur das la base de donnée
    #   elle return False en cas d'erreur grave, sinon elle retourne le status de l'enregistrement
    #   sous forme de string 
    ###################################################
    def register(self, param: str=None) -> str: # param = string de username/@username
        if(param == None):
            return False

        # si il est présent on retir le '@' l'api twitter n'en n'a pas besion !
        if(param.startswith("@")):
            param = param.replace('@', '')

        # on vérifie que l'utilisateur n'existe pas déjà dans la base
        if self.bdd.searchData(TweeterUser(0, username=param), userName=True) == False:
            # on requete chez twitter le nom de l'utilisateur
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

    ######################################################
    # la méthode getUserNameById est une interface qui demande à la classe TwitterApi
    #   de faire une requete user par son id plutôt que par son nom
    #   elle return le nom d'utilisateur en format string
    ######################################################
    def getUserNameById(self, id: int = 0) -> str:
        user = self.twp.userRequestById(id)['data']
        return(user['username'])

    ######################################################
    #   la méthode scrapTweets est une interface qui demande à la classe dataBase 
    #   de récupérer les infos de tous les users de la base de donnée
    #   
    ######################################################
    def scrapTweets(self):
        users = self.bdd.getUserData()

        for u in users:
            usr = TweeterUser(u['id'], desc=u['description'], name=u['user'], created_at=u['created_at'], username=u['username'])
            tweets = self.twp.tweetsRequest(usr.getId())
            for t in tweets['data']:
                if t['text'].find(self.modiese) != -1:
                    try:
                        twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'], referenced_tweets=t['referenced_tweets'][0]['id'], author_id=t['author_id'], type=t['referenced_tweets'][0]['type'])
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
        self.bdd.updateData(TweetObj(tweet['id'], text=tweet['text'], created_at=tweet['created_at'], pushed=1, author_id=tweet['author_id'],
        referenced_tweets=tweet['referenced_tweets'], type=tweet['type']))
        # except:
        #     self.bdd.updateData(TweetObj(tweet['id'], text=tweet['text'], created_at=tweet['created_at'], pushed=1, author_id=tweet['author_id']))
        return