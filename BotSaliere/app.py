from Controllers.twitterApiController import TwitterApi
from PyInclude import *

def main():
    twp = TwitterApi()
    rsp = twp.userRequest("NeoTastyNetwork")
    print(rsp)
    tweets = twp.tweetsRequest(rsp['data'][0]['id'])
    print(tweets)
    #print(rsp['data'][0]['id'])
    # rsp = twp.userRequest("NeoTastyNetwork")
    # print(rsp.__getitem__(1))

main()
