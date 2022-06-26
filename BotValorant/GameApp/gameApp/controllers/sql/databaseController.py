import pyodbc
from GameApp.gameApp.controllers.dataBaseController import dataBase
from GameApp.gameApp.dataModel.playerModel import Player

class dataBaseController:
    # Definition :
    #   conn = la string de connexion SQL utiliser pour faire le lien avec la bdd 
    #   cursor = c'est l'interface de commande sql pour toutes les requêtes 

    def __init__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};Server=DELKEIS_DESKTOP;Database=ProjetA;Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    # On récupère le contenu des tables sql pour mettre à jour la bdd temporaire
    # La fonction est voué à disparaître une fois la bdd stable
    def extractDb(self):
        self.cursor.execute('SELECT * FROM player')

        # tmpDb est initialisé ici de manière temporaire
        # il sera passé en argument de la structure une fois le databaseController stable
        #  def __init__(self, db = dataBase())
        tmpDb = dataBase()

        for item in self.cursor:
            # structure Player temporaire "se discard en fin de fonction"
            playerItem = Player(item['username'], item['userlevel'], item['xp'], item['discordId'], item['riotId'], item['riotPuuid'])

            # on vérifie si le joueur existe déja ou non dans la base temporaire 
            if tmpDb.searchData(playerItem.getDiscordId()) == True:
                if tmpDb.updateData(playerItem) == False:
                    # si on à trouver l'entrée mais que update return False
                    # on à une inchoérance
                    print("Erreur D'update")
                    return(False)
                else:
                    tmpDb.dumpData()
                    return(True)
            else:
                tmpDb.appendData(playerItem)
                tmpDb.dumpData()
                print("ajout de l'entrée") 


db = dataBaseController()
db.extractDb()



#try:
#    conn = pyodbc.connect('Driver={SQL Server};Server=DELKEIS_DESKTOP;Database=ProjetA;Trusted_Connection=yes;')
#except:
#    print("mauvais arguments !")
#    exit()

#cursor = conn.cursor()


#cursor.execute('''INSERT INTO player
#                  VALUES (?, ?, ?, ?, ?, ?, ?)''', 
#                (id, name, lvl, xp, did, rid, puuid))
#cursor.execute('SELECT * FROM player')

#for i in cursor:
#    print(i)

