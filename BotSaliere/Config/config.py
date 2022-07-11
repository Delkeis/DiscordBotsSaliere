import configparser

###############################################
#   la classe ConfigMod est une classe qui permet de lire, ecrir
#   et modifier le fichier de configuration
###############################################
class ConfigMod:
    # le nom du fichier est définit par filename 
    # si il n'existe pas il sera créer mais vide 
    fileName = "config.ini"

    def __init__(self):
        try:
            f = open(self.fileName, "r")
            f.close()
            self.openFile()
        except:
            self.setInitConfig()

    ##################################################
    #   la méthode SetInitConfig sert à la
    #   Construction initial du fichier de configuration
    #   si celui-ci n'existe pas encore
    ##################################################
    def setInitConfig(self):
        with open(self.fileName, "w") as configObject:
            self.configFile = configparser.ConfigParser()
        print("config file Created")
        #On ouvre le fichier nouvellement créer en lecture uniquement
        self.openFile()

    #############################################################
    #   méthode permettant d'ouvrir le fichier de config au besion
    #
    #############################################################
    def openFile(self):
        self.configFile = configparser.ConfigParser()
        self.configFile.read(self.fileName)

    ###########################################################
    #   la méthode getParameter sert à récupérer un paramètre 
    #   précis dans le fichier de configuration 
    ###########################################################
    def getParameter(self, param, section="DevConfig"):
        try:
            return(self.configFile[section][str(param)])
        except:
            print("paramètre "+ str(param)+" non trouver !")
            return(False)
