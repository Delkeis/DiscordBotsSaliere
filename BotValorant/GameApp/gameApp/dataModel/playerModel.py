# La classe player est une définition de chaque joueur et de ses informations 
# fidèle aux entrées dans la base de donée ou du fichier de stckage
#
class Player:
    def __init__(self, name="", level=0, xp=0, discordId="", riotId="", riotPuuid=""):
        self.name = name            # nom du joueur 
        self.level = level          # niveau du joueur 
        self.xp = xp                # xp du joueur 
        self.discordId = discordId  # nom sur le serveur discord sous forme @nom#chiffre
        self.riotId = riotId        # nom du compte riot sous forme nom#tag
        self.riotPuuid = riotPuuid  # Personnal Unique User ID du compte riot

    def setName(self, name):
        self.name = name

    def getName(self):
        return (self.name)

    def setLevel(self, level):
        self.level = level
    
    def getLevel(self):
        return (self.level)

    def setXp(self, xp):
        self.xp = xp
    
    def getXp(self):
        return (self.xp)

    def setDiscordId(self, discordId):
        self.discordId = discordId
    
    def getDiscordId(self):
        return (self.discordId)

    def setRiotId(self, riotId):
        self.riotId = riotId
    
    def getRiotId(self):
        return (self.riotId)
    
    def setRiotPuuid(self, riotPuuid):
        self.riotPuuid = riotPuuid
    
    def getRiotPuuid(self):
        return (self.riotPuuid)