from BotSaliere.dataModel.tweet import TweetObj

class SubTweetObject(TweetObj):
    def __init__(self, id, text=None, created_at=None, pushed=0, subTweet=True):
        self.setText(text)
        self.setCreated_at(created_at)
        self.setPushed(pushed)
        self.setId(id)
        self.subTweet = subTweet

    def getSubTweet(self):
        return self.subTweet
    def setSubTweet(self, subTweet):
        self.subTweet = subTweet
