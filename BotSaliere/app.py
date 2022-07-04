from Controllers.twitterApiController import TwitterApi
from PyInclude import *

def main():
    bdd = dataBase()
    twp = TwitterApi()
    rsp = twp.userRequest("NeoTastyNetwork")
    print("===================================")
    print(rsp)
    print("===================================")
    usr = TweeterUser(rsp['data'][0]['id'], desc=rsp['data'][0]['description'], name=rsp['data'][0]['name'],
                        created_at=rsp['data'][0]['created_at'], username=rsp['data'][0]['username'])
    print(rsp)
    if bdd.searchData(usr) == False:
        bdd.appendData(usr)
    tweets = twp.tweetsRequest(usr.getId())

    for t in tweets['data']:
        twt = TweetObj(t['id'], text=t['text'], created_at=t['created_at'])
        if bdd.searchData(twt) == False:
            bdd.appendData(twt)
        
    print(tweets)
    #print(rsp['data'][0]['id'])
    # rsp = twp.userRequest("NeoTastyNetwork")
    # print(rsp.__getitem__(1))

main()
