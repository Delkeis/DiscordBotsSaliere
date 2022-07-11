from Controllers.twitterApiController import TwitterApi
from Controllers.bddController import dataBase
from dataModel.twitterUser import TwitterUser
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
        if self.bdd.searchData(TwitterUser(0, username=param), userName=True) == False:
            # on requete chez twitter le nom de l'utilisateur
            req = self.twp.userRequest(param)
            try:
                usr = TwitterUser(req['data'][0]['id'], desc=req['data'][0]['description'], name=req['data'][0]['name'],
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
    ######################################################
    def scrapTweets(self):
        users = self.bdd.getUserData()

        # on parcours tous les utilisateurs de la bdd
        for u in users:
            usr = TwitterUser(u['id'], desc=u['description'], name=u['user'], created_at=u['created_at'], username=u['username'])
            tweets = self.twp.tweetsRequest(usr.getId())

            # on parcours tous les tweets de l'utilisateur u
            for t in tweets['data']:

                if t['text'].find(self.modiese) != -1:
                    # on utilise un  try except pour controller si le tweet contiens une référence à un autre tweet
                    try:
                        twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'], referenced_tweets=t['referenced_tweets'][0]['id'],
                            author_id=t['author_id'], type=t['referenced_tweets'][0]['type'])
                    except:
                        twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'], author_id=t['author_id'])

                    # on verifie si il n'est pas déja dans la base pour le réinscrire
                    if self.bdd.searchData(twt) == False:
                        self.bdd.appendData(twt)
        return

    ########################################################
    #   la méthode pullTweets sert d'interface pour récupérer les tweets
    #   depuis la base de donnée
    ########################################################
    def pullTweets(self):
        return(self.bdd.getTweetData())
    
    ########################################################
    #   la méthode validateTweet est une interface avec la bdd 
    #   pour mettre à jour la variable pushed dans la base
    ########################################################
    def validateTweet(self, tweet):
        self.bdd.updateData(TweetObj(tweet['id'], text=tweet['text'], created_at=tweet['created_at'], pushed=1, author_id=tweet['author_id'],
        referenced_tweets=tweet['referenced_tweets'], type=tweet['type']))
        return