from logging import ERROR
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
import os



class TwitterWatchDog:
    def __init__(self):
        '''
        consumer ID may expire soon, 
        note to self: renew consumer key next week
        '''

        consumerkey='YqS2TrnxOfCq0RuhhH3LuanFm'
        consumersecretkey='YHoaoUqFPWBJJO0kWHiqhiSLCRlsCKbSvwYCuqYywwuquCab0I'
        APIKEY='1279396464540520448-uKfqpyReeahHxbNgy1jFWEP1rzw1ym'
        APISECRETKEY='DmynSRa0CrBxABmeMIsvl5xD6XJDdZ750tPqTHw1qAWUy'
        try: 
            self.auth = OAuthHandler(consumerkey, consumersecretkey) 
            self.auth.set_access_token(APIKEY, APISECRETKEY) 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 
    def clean_tweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])(\w+:\/\/\S+)", " ", tweet).split())
    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''

        analysis = TextBlob(self.clean_tweet(tweet)) 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'
    def get_tweets(self, query, count = 10): 

        tweets = [] 
  
        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 
  
            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 
  
                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 
  
                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 

            return tweets 
  
        except tweepy.TweepError as e: 
            print("Error : " + str(e))

def main(x): 
    # creating object of TwitterClient Class 
        api = TwitterWatchDog() 
    #create list to store data
        tweetdata = list()
    #call tweet
        tweets = api.get_tweets(query = x, count = 200) 
        tweetdata.append(tweets)
    # picking positive tweets from tweets 
        ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
        tweetdata.append("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
        ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
        tweetdata.append("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
        tweetdata.append("Neutral tweets percentage: {} % \ ".format(100*(len(tweets) -(len( ntweets )+len( ptweets)))/len(tweets))) 
  
        tweetdata.append("\n\nPositive tweets:") 
        for tweet in ptweets[:10]: 
            tweetdata.append(tweet['text']) 
  
   
        tweetdata.append("\n\nNegative tweets:") 
        for tweet in ntweets[:10]: 
            tweetdata.append(tweet['text']) 
        return tweetdata


class scraper:
    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0'}
    def get(self,URL):
        if 'https://' not in URL:
            URL = 'https://' + URL
        page = requests.get(URL,headers=self.header)
        soup = BeautifulSoup(page.content, "html.parser",)
        return(soup)
 
    def auth_get(self,username,password,url,auth_website = ''):
        print('currently implements logins are:')
        print('1.github 2.twitter, 3.manual')
        website = input('choose a website')
        if website == 1:
            requests.get('https://api.github.com/user', auth=HTTPBasicAuth(username, password),headers=self.header)
            self.get(url)
        elif website == 2:
            url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
            auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
                      'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
            requests.get(url, auth=auth,headers=self.header)
            self.get(url)
        elif website == 3:
            requests.get(auth_website, auth=HTTPBasicAuth(username, password),headers=self.header)
        pass    

scraper = scraper()

def save(inp):
    x = input('would you like to save the output to a database? y/n')
    if x =='y':
        name=input('name for file in storage?')
        with open(name + '.txt', 'x') as f:
            f.write(str(inp))
            f.close()
        print('data was written to file')
        os.system('open ' + name +'.txt')
    else:
        exit()

while True:
    action = input('choose an action')
    if action == 'get':
        i = input('insert website: ')
        print(scraper.get(i))
    elif action == 'sentiment':
        xi = input('type a word to check its sentimental use on twitter')
        print(main(xi))