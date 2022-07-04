import configparser

class ConfigMod:
    fileName = "config.ini"

    def __init__(self):
        try:
            f = open(self.fileName, "r")
            f.close()
            self.openFile()
        except:
            self.setInitConfig()

    #Construction initial du fichier de configuration
    def setInitConfig(self):
        with open(self.fileName, "w") as configObject:
            self.configFile = configparser.ConfigParser()
        print("config file Created")
        #On ouvre le fichier nouvellement créer e nlecture uniquement
        self.openFile()

    #Fonction permettant d'ouvrir le fichier de config au besion
    def openFile(self):
        self.configFile = configparser.ConfigParser()
        self.configFile.read(self.fileName)


    def printContent(self):
        print("--content--")
        print(self.configFile)

    def getParameter(self, param, section="DevConfig"):
        try:
            return(self.configFile[section][str(param)])
        except:
            print("paramètre "+ str(param)+" non trouver !")
            return(False)
