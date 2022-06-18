from GameApp.gameApp.PyInclude import *
import json

#
#   La classe GameApp est la classe principale qui permet de controller 
#   les différents aspects du jeu / bot 
#       bdd
#       gamerules
#       apicall
#

class GameApp:
    #   definition 
    #       conf : module de récupération des configurations 
    #       bdd  : module de gestion de la base de donnée
    #       rapi : module de gestion de l'api de riot
    #

    def start(self):
        self.conf = ConfigMod()
        self.bdd = dataBase()
        self.rapi = riotApi(self.conf.getParameter("riotApiKey"))
    
    def newComm(self, myStr):
        myStr = myStr.replace('#', '/')
        self.rapi.composeUri("account/v1", "accounts/by-riot-id", myStr)
        return(self.rapi.postUri())

    # commande qui permet d'entrée un nouvel utilisateur dans la base de donnée
    def register(self, userId):
        if self.bdd.searchData(userId) == False:

            uriname = userId.replace('#', '/')
            self.rapi.composeUri("account/v1", "accounts/by-riot-id", uriname)

            myName = userId.split('#')[0]
            rep = self.rapi.postUri()

            pl = Player(myName, 0, 0, userId, userId, rep['puuid'])
            self.bdd.appendData(pl)
            self.bdd.dumpData()
            print("Register : "+ userId+" in the DataBase")
        else:
            print("l'utilisateur existe déjà")
