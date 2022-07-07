from dataModel.subTweet import SubTweetObject
from dataModel.tweeterUser import TweeterUser
from dataModel.tweet import TweetObj
import json 

class dataBase:
    #Definition 
    # tab  bd [
    #           "name",
    #           "level",
    #           "xp",
    #           "discordId",
    #           "riotId",
    #           "riotPuuid"
    #         ]

    def __init__(self):
        self.path = ".\\tmp\\tmpBd.json"
        with open(self.path, 'r+') as f:
            self.bd = json.load(f)
        print("------db init-------")

    #ajoute une donnée dans le pool disponible
    def appendData(self, object=None):
        # je vérifie de quel type est l'objet en entrée
        # Si c'est un user on ajoute les donées dans la partie user 
        # si c'est un tweet on ajoute les données dans la partie tweet
        # sinon on retourne false car l'objet n'est pas bon
        if type(object) == type(TweeterUser(0)):
            self.bd['user'].append({
                "id": object.getId(),
                "username": object.getUserName(),
                "user": object.getName(),
                "created_at": object.getCreated_At().replace('T', ' ').replace('.000Z', ''),
                "description": object.getDesc()
            })
        elif type(object) == type(TweetObj(0)):
            self.bd['tweet'].append({
                "id": object.getId(),
                "created_at": object.getCreated_At().replace('T', ' ').replace('.000Z', ''),
                "text": object.getText(),
                "referenced_tweets": object.getReferenced_Tweets(),
                "pushed": object.getPushed()
            })
        elif type(object) == type(SubTweetObject(0)):
            self.bd['subtweet'].append({
                "id": object.getId(),
                "created_at": object.getCreated_At().replace('T', ' ').replace('.000Z', ''),
                "text": object.getText(),
                "pushed": object.getPushed()
            })      
        else:
            print("le type de data n'est pas bon")
            return(False)
        self.dumpData()



    #permet de rechercher une entrée dans la base de donnée via l'id
    def searchData(self, object=None, userName=False):
        # on modifie d'abbord la variable myType qui indique
        # si mon object est un user ou un tweet
        if type(object) == type(TweeterUser(0)):
            myType = 'user'
        elif type(object) == type(TweetObj(0)):
            myType = 'tweet'
        elif type(object) == type(SubTweetObject(0)):
            myType = 'subtweet'
        else:
            return (False)

        y = False
        # on parcours toute la base de donnée jusqu'à  soit trouver l'entrée
        # soit jusqu'à la fin
        if userName == False:
            for i in self.bd.get(myType):
              if i['id'] == object.getId():
                    y = True
                    break
            return(y)
        elif userName == True:
            for i in self.bd.get(myType):
              if i['username'] == object.getUserName():
                    y = True
                    break
            return(y)

    def getUserData(self):
        return(self.bd['user'])

    def getTweetData(self, object=None):
        if  object == None:
            return(self.bd['tweet'])

        elif type(object) == type(TweetObj(0)):
            myType = 'tweet'
        elif type(object) == type(SubTweetObject(0)):
            myType = 'subtweet'

        for t in self.bd[myType]:
            if t['id'] == object.getId():
                object.setText(t['text'])
                object.setCreated_At(t['created_at'])
                object.setPushed(t['pushed'])
                if myType == 'tweet':
                    object.setReferenced_Tweets(t['referenced_tweets'])
                return(object)



    def deleteData(self, object=None):
        if type(object) == type(TweeterUser(0)):
            myType = 'user'
        elif type(object) == type(TweetObj(0)):
            myType = 'tweet'
        else:
            return (False)

        i = 0

        if myType == 'user':
            while i < len(self.bd[myType]):
                if self.bd[myType][i]['user'] == object.getUser():
                    self.bd[myType].pop(i)
                i = i + 1
        elif myType == 'tweet':
            while i < len(self.bd[myType]):
                if self.bd[myType][i]['id'] == object.getId():
                    self.bd[myType].pop(i)
                i = i + 1

            return

    # prend en argument la structure User ou Tweet pour mettre à jour le fichier de bdd
    # La fonction n'est pas encore tester  
    def updateData(self, object=None):
        # on modifie d'abbord la variable myType qui indique
        # si mon object est un user ou un tweet
        if type(object) == type(TweeterUser(0)):
            myType = 'user'
        elif type(object) == type(TweetObj(0)):
            myType = 'tweet'
        else:
            return (False)

        y = False

        if (self.searchData(object) == True):
            cpt = 0
            while cpt < len(self.bd[myType]):
                if self.bd[myType][cpt]['id'] == object.getId():
                    if myType == 'user':
                        self.bd[myType][cpt] = {
                            "id": object.getId(),
                            "username": object.getUserName(),
                            "user": object.getName(),
                            "created_at": object.getCreated_At(),
                            "description": object.getDesc()
                            }
                    elif myType == 'tweet':
                        self.bd[myType][cpt] = {
                            "id": object.getId(),
                            "created_at": object.getCreated_At(),
                            "text": object.getText(),
                            "referenced_tweets": object.getReferenced_Tweets(),
                            "pushed": object.getPushed()
                            }
                cpt = cpt + 1
            self.dumpData()    
            return(True)
        else:
            return(False)

    #fixe les nouvelles entrées dans la base de donnée
    def dumpData(self):
        with open(self.path, 'r+') as f:
            json.dump(self.bd, f, indent=4, separators=(',', ': '))

