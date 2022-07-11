from dataModel.Obj import obj

############################### 
#   la classe TweetObj est une structure de 
#   donnée qui hérite de obj
###############################
class TweetObj(obj):
    def __init__(self, id, text:str=None, created_at:str=None, pushed=0, referenced_tweets=None, author_id=0, type:str='tweeted') -> None:
        self.text = text
        self.pushed = pushed
        self.referenced_tweets = referenced_tweets
        self.author_id = author_id
        self.type = type
        self.setCreated_At(created_at)
        self.setId(id)

    def getText(self) -> str:
        return(self.text)
    def setText(self, text) -> None:
        self.text = text

    def getPushed(self) -> int:
        return(self.pushed)
    def setPushed(self, pushed) -> None:
        self.pushed = pushed

    def getReferenced_Tweets(self) -> str:
        return(self.referenced_tweets)
    def setReferenced_Tweets(self, referenced_tweets) -> None:
        self.referenced_tweets = referenced_tweets

    def setAuthor_Id(self, id: int) -> None:
        self.author_id = id
    def getAuthor_Id(self) -> int:
        return self.author_id

    def setType(self, type:str) -> None:
        self.type = type
    def getType(self) -> str:
        return self.type