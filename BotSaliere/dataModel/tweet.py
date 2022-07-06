from BotSaliere.dataModel.Obj import obj

class TweetObj(obj):
    def __init__(self, id, text=None, created_at=None, pushed=0):
        self.text = text
        self.pushed = pushed
        self.setCreated_At(created_at)
        self.setId(id)

    def getText(self):
        return(self.text)
    def setText(self, text):
        self.text = text

    def getPushed(self):
        return(self.pushed)
    def setPushed(self, pushed):
        self.pushed = pushed