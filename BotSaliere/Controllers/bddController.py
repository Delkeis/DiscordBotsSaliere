from dataModel.twitterUser import TwitterUser
from dataModel.tweet import TweetObj
import json 

##########################################################
#   la classe DataBase sert à regrouper differents outils 
#   utils à la gestions de la base de donnée 
#   ATTENTION : la classe est voué à disparaître 
#       remplacer par des accèss SQL
##########################################################
class dataBase:
    # définition de la base de donnée
    #{
    #     "user": [{
    #             "id": "",
    #             "username": "",
    #             "user": "",
    #             "created_at": "",
    #             "description": ""
    #         }],
    #     "info": [{
    #             "hashtag": ""
    #         }],
    #     "tweet": [{
    #             "id": "",
    #             "created_at": "",
    #             "text": "",
    #             "referenced_tweets": 33,
    #             "type": "",
    #             "author_id": "",
    #             "pushed": 0
    #         }]
    # }

    def __init__(self):
        self.path = ".\\tmp\\tmpBd.json"
        with open(self.path, 'r+') as f:
            self.bd = json.load(f)
        print("------db init-------")

    ###################################################
    #   la méthode appendData sert à 
    #   ajouté une donnée dans la base de donnée
    ###################################################
    def appendData(self, object=None) -> bool:
        # je vérifie de quel type est l'objet en entrée
        if type(object) == type(TwitterUser(0)):
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
                "type": object.getType(),
                "author_id": object.getAuthor_Id(),
                "pushed": object.getPushed()
             })
        else:
            print("le type de data n'est pas bon")
            return(False)
        self.dumpData()
        return(True)


    #####################################################
    #   la methode searchData permet de rechercher une entrée dans la base de donnée via l'id
    #   ou le user name si la variable userName n'est plus égale à False 
    ####################################################
    def searchData(self, object=None, userName=False) -> bool:

        if type(object) == type(TwitterUser(0)):
            myType = 'user'
        elif type(object) == type(TweetObj(0)):
            myType = 'tweet'
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

    ####################################################
    #   la méthode getUserData retourne le contenu de la base user
    #   sous forme de liste
    ####################################################
    def getUserData(self) -> list:
        return(self.bd['user'])

    ####################################################
    #   la méthode getTweetData retourne le contenu de la base tweet
    #   sous forme de liste si aucun object n'est rensegnier 
    #   sinon retrourne l'objet unique avec les infos mis à jour
    ####################################################
    def getTweetData(self, object=None):
        if  object == None:
            return(self.bd['tweet'])

        elif type(object) == type(TweetObj(0)):
            myType = 'tweet'

        for t in self.bd[myType]:
            if t['id'] == object.getId():
                object.setText(t['text'])
                object.setCreated_At(t['created_at'])
                object.setPushed(t['pushed'])
                object.setAuthor_Id(t['author_id'])
                if myType == 'tweet':
                    object.setReferenced_Tweets(t['referenced_tweets'])
                    object.setType(t['type'])
                return(object)


    #####################################################
    #   la méthode deleteData supprime de la base l'objet 
    #   en argument 
    #####################################################
    def deleteData(self, object=None):

        # onvérifie le type de l'objet
        if type(object) == type(TwitterUser(0)):
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

        return(True)

    ###############################################
    # prend en argument la structure User ou Tweet pour mettre à jour le fichier de bdd
    # 
    ###############################################
    def updateData(self, object=None) -> bool:

        if object == None:
            return
        if type(object) == type(TwitterUser(0)):
            myType = 'user'
        elif type(object) == type(TweetObj(0)):
            myType = 'tweet'
        else:
            return (False)

        y = False
        # on verifi que l'objet existe dans la base
        if (self.searchData(object) == True):
            cpt = 0

            #on vérifie toutes les entrées de la base pour trouver la bonne  
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
                            "type": object.getType(),
                            "author_id": object.getAuthor_Id(),
                            "pushed": object.getPushed()
                            }
                cpt = cpt + 1
            self.dumpData()    
            return(True)
        else:
            return(False)

    ##############################################
    #   la méthode get_setinfos() sert à changer ou récupérer 
    #   la partie info de la base nottement "hashtag"
    ##############################################
    def get_setInfos(self, set=False, nfo:str=None) -> str:
        if set == False:
            return(self.bd["info"][0]["hashtag"])
        else:
            self.bd["info"][0] = {"hashtag": nfo}
            self.dumpData()

    ##################################################
    #fixe les nouvelles entrées dans la base de donnée
    #
    ##################################################
    def dumpData(self):
        with open(self.path, 'r+') as f:
            json.dump(self.bd, f, indent=4, separators=(',', ': '))

