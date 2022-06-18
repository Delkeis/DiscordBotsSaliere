import requests

#
#   la classe RiotApi permet d'ajouter des appels sur l'api de riot 
#   et de composer les urls d'appel 
#
class riotApi:
    #définition de la classe 
    # str uri
    # str uriBase = "https://europe.api.riotgames.com/riot"
    # str object = ""
    # str method = ""
    # str apiKey = ""

    def __init__(self, apiKey=""):
        self.uri = False
        self.apiKey = apiKey
        self.uriBase = "https://europe.api.riotgames.com/riot"
        print("start riot api Module !")

    # permet de moduler l'appel en modifiants les valeurs par défault
    def composeUri(self, object="account/v1", method="accounts/by-riot-id", riotId="delkeis/euw"):
        self.uri = self.uriBase+"/"+object+"/"+method+"/"+riotId+"?api_key="+self.apiKey

    # fonction de débug pour récupérer l'url générer
    def printUri(self):
        print(self.uri)

    # envoie la requète sous forme Get
    # renvoie -1 en cas d'érreur
    # renvoie le résultat de la réquête sous format json en cas de réussite !
    def postUri(self):
        if self.uri != False:
            rep = requests.get(self.uri)
            self.uri = False
            if(rep.status_code == 200):
                return(rep.json())
            else:
                print("error "+str(rep.status_code)+" find!")
                print(rep.content)
                return(-1)
        else:
            print("Mauvais Url !")
            return(-1)