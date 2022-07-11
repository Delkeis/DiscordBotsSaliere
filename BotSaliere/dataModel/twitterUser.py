from dataModel.Obj import obj

###############################
#   la classe TwitterUser est une structure de donnée
#   qui hérite de la classe obj
###############################
class TwitterUser(obj):
    def __init__(self, id, desc=None, name=None, created_at=None, username=None):
        self.description = desc
        self.name = name
        self.setCreated_At(created_at)
        self.setId(id)
        self.userName = username

    def getDesc(self):
        return(self.description)
    def setDesc(self, description):
        self.description = description

    def getName(self):
        return(self.name)
    def setName(self, name):
        self.name = name


    def getUserName(self):
        return(self.userName)
    def setUsername(self, userName):
        self.userName = userName