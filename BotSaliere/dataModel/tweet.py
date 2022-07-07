from dataModel.Obj import obj

class TweetObj(obj):
    ##
    #   Erited :    - getId()
    #               - setId(Int)
    #               - obj.Id
    ##
    def __init__(self, id, text=None, created_at=None, pushed=0, referenced_tweets=None):
        self.text = text
        self.pushed = pushed
        self.referenced_tweets = referenced_tweets
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

    def getReferenced_Tweets(self):
        return(self.referenced_tweets)
    def setReferenced_Tweets(self, referenced_tweets):
        self.referenced_tweets = referenced_tweets