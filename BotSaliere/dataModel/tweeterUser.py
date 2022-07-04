class TweeterUser:
    def __init__(self, id, desc=None, name=None, created_at=None, username=None):
        self.description = desc
        self.name = name
        self.created_at = created_at
        self.id = id
        self.userName = username

    def getDesc(self):
        return(self.description)
    def getName(self):
        return(self.name)
    def getCreated_at(self):
        return(self.created_at)
    def getId(self):
        return(self.id)
    def getUserName(self):
        return(self.userName)