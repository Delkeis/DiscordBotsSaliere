from requests_oauthlib import OAuth1Session
from Config.config import ConfigMod

#################################################################
#   la classe twitterApi regroupe les outils pour fais des requetes 
#   et autres interaction avec l'api Twitter 
#################################################################
class TwitterApi:

    def __init__(self):
        self.configFile = ConfigMod()
        self.consumer_key=self.configFile.getParameter("twitterApiKey")
        self.consumer_secret=self.configFile.getParameter("twitterApiSecretKey")
        self.initUser()

        # Get request token
        self.request_token_url = "https://api.twitter.com/oauth/request_token"
        self.oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret)
        try:
            self.fetch_response = self.oauth.fetch_request_token(self.request_token_url)
        except ValueError:
            print(
            "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        self.resource_owner_key = self.fetch_response.get("oauth_token")
        self.resource_owner_secret = self.fetch_response.get("oauth_token_secret")
        self.getAuth()

    #################################################################
    #   la méthode initUser sert à initialiser les paramètres 
    #   des requêtes users
    #################################################################
    def initUser(self, username: str = "Delkeis") -> None:
        self.fields = "created_at,description"
        self.twtf = "created_at"
        self.users = username
        self.params = {"usernames": self.users, "user.fields": self.fields, "tweet.fields": self.twtf}

    #################################################################
    #   la méthode getAuth sert à faire la reqête de demande  
    #   d'acces à l'api twitter 
    #################################################################
    def getAuth(self):
        print("Got OAuth token: %s" % self.resource_owner_key)

        # # Get authorization
        self.base_authorization_url = "https://api.twitter.com/oauth/authorize"
        self.authorization_url = self.oauth.authorization_url(self.base_authorization_url)
        print("Please go here and authorize: %s" % self.authorization_url)
        self.verifier = input("Paste the PIN here: ")

        # Get the access token
        self.access_token_url = "https://api.twitter.com/oauth/access_token"
        self.oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.resource_owner_key,
            resource_owner_secret=self.resource_owner_secret,
            verifier=self.verifier,
        )
        self.oauth_tokens = self.oauth.fetch_access_token(self.access_token_url)

        self.access_token = self.oauth_tokens["oauth_token"]
        self.access_token_secret = self.oauth_tokens["oauth_token_secret"]

    #################################################################
    #   la méthode userRequest sert à faire la requête pour les utilisateur  
    #   à partir du username 
    #################################################################
    def userRequest(self, username: str=None):
        if username != None:
            self.initUser(username)
        # Make the request
        self.oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )

        self.response = self.oauth.get(
            "https://api.twitter.com/2/users/by", params=self.params
        )

        if self.response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(self.response.status_code, self.response.text)
            )
        print("Response code: {}".format(self.response.status_code))
        return(self.response.json())

    #################################################################
    #   la méthode userRequestById sert à faire une requête du user via 
    #   son Id Twitter 
    #################################################################
    def userRequestById(self, id: int):

        self.oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )

        self.response = self.oauth.get(
            "https://api.twitter.com/2/users/{}".format(id)
        )
        if self.response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(self.response.status_code, self.response.text)
            )
        print("Response code: {}".format(self.response.status_code))
        return(self.response.json())

    #################################################################
    #   ma méthode tweetsRequest sert à faire les requêtes des tweets 
    #   via l'userId Twitter
    #################################################################
    def tweetsRequest(self, userId):
        userId = str(userId)
        self.oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=self.access_token,
            resource_owner_secret=self.access_token_secret,
        )

        prm = {"tweet.fields": "created_at,referenced_tweets", "expansions": "author_id"}

        self.response = self.oauth.get(
            "https://api.twitter.com/2/users/{}/tweets".format(userId), params=prm
        )
        if self.response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(self.response.status_code, self.response.text)
            )
        print("Response code: {}".format(self.response.status_code))
        return(self.response.json())