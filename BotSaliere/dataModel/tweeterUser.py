from BotSaliere.dataModel.Obj import obj

class TweeterUser(obj):
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