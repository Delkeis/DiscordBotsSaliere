from GameApp.gameApp.dataModel.playerModel import Player
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
    def appendData(self, player: Player):
        self.bd['player_data'].append({
            "name": player.getName(),
            "level": player.getLevel(),
            "xp": player.getXp(),
            "discordId": player.getDiscordId(),
            "riotId": player.getRiotId(),
            "riotPuuid": player.getRiotPuuid()
        })

    #permet de rechercher une entrée dans la base de donnée via le RiotId
    def searchData(self, searchStr):
        y = False

        for i in self.bd.get('player_data'):
          if i['riotId'] == searchStr or i['discordId'] == searchStr:
                y = True
                break
        return(y)

    #fixe les nouvelles entrées dans la base de donnée
    def dumpData(self):
        with open(self.path, 'r+') as f:
            json.dump(self.bd, f, indent=4, separators=(',', ': '))