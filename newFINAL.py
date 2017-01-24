import tweepy
import datetime
import feedparser
import time
import twitter
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

from TwitterSearch import *

try:
    auth = tweepy.OAuthHandler('5yiBL7NeknLbuVGtwxqoXZy9R', 'LhDwfokNrFVQduvBt68ewTWlUx9ScvRnCF94XmMhUjQYn5UuaZ')
    auth.set_access_token('822127681810681859-sAV7x2TJxt70K7b2CsvxdXjDwaWD1Ar', 'dDSPQ8sKKx2479JRvUJPzvJFHsiGYRIMHk6WgW64gfbxQ')
    api = tweepy.API(auth)

    #api.update_status('Hello! Cypress is happy to help. Tag this twitter handle, tweet with keywords for help, for supp. give initials of Dept. \n' + unicode(datetime.datetime.now().date()))

    d = feedparser.parse('http://origin-www.cypress.com/feed/blog/all')  # for rss feeds from Cypress.com
    leng = len(d['entries'])

    tso = TwitterSearchOrder()                                   # create a TwitterSearchOrder object
    tso.set_keywords(['@Abhinav_K_007', ''])
    tso.set_language('en')                                       # we want to see German tweets only
    tso.set_include_entities(True)                               # and don't give us all those entity information

    ts = TwitterSearch(
        consumer_key='5yiBL7NeknLbuVGtwxqoXZy9R',
        consumer_secret='LhDwfokNrFVQduvBt68ewTWlUx9ScvRnCF94XmMhUjQYn5UuaZ',
        access_token='822127681810681859-sAV7x2TJxt70K7b2CsvxdXjDwaWD1Ar',
        access_token_secret='dDSPQ8sKKx2479JRvUJPzvJFHsiGYRIMHk6WgW64gfbxQ'
     )

    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s,%s' % ( tweet['user']['screen_name'], tweet['text'] , tweet['id']) )
        if ('Memo' in tweet['text'] or 'memo' in tweet['text'] or 'MEMO' in tweet['text']):
            print 'follow link- http://doc.cypress.com'
            api.update_status('@' + tweet['user']['screen_name'] + ' Hello follow http://doc.cypress.com \n' + unicode(datetime.datetime.now()),in_reply_to_status_id=tweet['id'])
        elif ('ECN' in tweet['text'] or 'Ecn' in tweet['text'] or 'ecn' in tweet['text']):
            print 'follow link- http://change.cypress.com'
            api.update_status('@' + tweet['user']['screen_name'] + ' Hello follow http://change.cypress.com \n' + unicode(datetime.datetime.now()), in_reply_to_status_id=tweet['id'])
        elif ('Dept' in tweet['text'] or 'Dept-Head' in tweet['text'] or 'Support'in tweet['text']):
            if 'HR' in tweet['text']:
                api.update_status('@' + tweet['user']['screen_name'] + ' Hello contact @RJTO \n' + unicode(datetime.datetime.now()), in_reply_to_status_id=tweet['id'])
            if 'ITG' in tweet['text']:
                api.update_status('@' + tweet['user']['screen_name'] + ' Hello contact @VNS \n' + unicode(datetime.datetime.now()),in_reply_to_status_id=tweet['id'])
        else:
            api.update_status('@' + tweet['user']['screen_name'] + ' Hello contact @CY_HELP \n' + unicode(datetime.datetime.now()),in_reply_to_status_id=tweet['id'])

    for x in range(leng):
        api.update_status('Hi Folks, ' + d['entries'][x]['title'] + '\n' + d.entries[x]['link'] + unicode(datetime.datetime.now().time()))
        time.sleep(1*60)

except TwitterSearchException as e:
    print(e)