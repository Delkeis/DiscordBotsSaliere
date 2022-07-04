class TweetObj:
    def __init__(self, id, text=None, created_at=None):
        self.text = text
        self.created_at = created_at
        self.id = id
        self.pushed = 0

    def getText(self):
        return(self.text)
    def getCreated_at(self):
        return(self.created_at)
    def getId(self):
        return(self.id)
    def getPushed(self):
        return(self.pushed)