from dataModel.tweet import TweetObj

class SubTweetObject(TweetObj):
    def __init__(self, id, text=None, created_at=None, pushed=0, referenced_tweets=None, subTweet=True, author_id=0):
        self.setText(text)
        self.setCreated_At(created_at)
        self.setPushed(pushed)
        self.setId(id)
        self.setReferenced_Tweets(referenced_tweets)
        self.setAuthor_Id(author_id)
        self.subTweet = subTweet

    def getSubTweet(self):
        return self.subTweet
    def setSubTweet(self, subTweet):
        self.subTweet = subTweet
