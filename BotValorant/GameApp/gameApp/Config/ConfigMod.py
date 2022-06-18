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
            self.configFile.add_section("DevConfig")
            self.configFile.set("DevConfig", "apiKey", "'clé d'api ici'")
            self.configFile.set("DevConfig", "riotApiKey", "riot")
            self.configFile.write(configObject)
            configObject.flush()
            configObject.close()
        print("config file Created")
        #On ouvre le fichier nouvellement créer e nlecture uniquement
        self.openFile()

    #Fonction permettant d'ouvrir le fichier de config au besion
    def openFile(self):
        self.configFile = configparser.ConfigParser()
        self.configFile.read(self.fileName)
        print("file "+self.fileName+" opened !")

    def printContent(self):
        print("--content--")
        print(self.configFile)

    def getParameter(self, param, section="DevConfig"):
        try:
            return(self.configFile[section][str(param)])
        except:
            print("paramètre "+ str(param)+" non trouver !")

    #Destructeur de fin d'execution
    #def __del__(self):
        #self.configFile.close()
        #print("close config file--")