from PyInclude import *

def main():
    print("start")
    configFile = ConfigMod()

    auth = tweepy.OAuthHandler(configFile.getParameter("twitterApiKey"), configFile.getParameter("twitterApiSecretKey"))
    auth.set_access_token(configFile.getParameter("twitterAccessToken"), configFile.getParameter("twitterAccessTokenSecret"))

    api = tweepy.API(auth)
    api.verify_credentials()
    try:
        print(api.verify_credentials())
        print('successful auth !')
    except:
        print('auth fail !')

main()