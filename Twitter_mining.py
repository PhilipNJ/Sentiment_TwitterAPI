import pandas as pd
import tweepy

 
consumer_key = 'QZe3I2kU76MkQU0WJviuimYmc'
consumer_secret = 'gnoHkirwZeDHSEMh0HDge7ifk1SKSrwKnRtIf1IYdDpCwzekYf'
access_key = '1018711747027296256-PW41Eb1LulZ6DEti93ZUyEWvIh8ulP'
access_secret = 'RrelUsVAdWpA48bAcWqmaJFgoGLFEdAGxQVFzqx7ROR93'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# function to perform data extraction
def scrape(words, date_since, numtweet):
        # Creating DataFrame using pandas
        db = pd.DataFrame(columns=['username','description', 'location','following','followers','totaltweets','retweetcount'])
 
        tweets = tweepy.Cursor(api.search_tweets, words, lang="en",since_id=date_since,tweet_mode='extended').items(numtweet)

        list_tweets = [tweet for tweet in tweets]

        i = 1
        for tweet in list_tweets:
                username = tweet.user.screen_name
                description = tweet.user.description
                location = tweet.user.location
                following = tweet.user.friends_count
                followers = tweet.user.followers_count
                totaltweets = tweet.user.statuses_count
                retweetcount = tweet.retweet_count

                ith_tweet = [username, description,
                             location, following,
                             followers, totaltweets,
                             retweetcount]

                db.loc[len(db)] = ith_tweet

                i = i+1

                print(db.shape)

                db.to_csv("tweets.csv")


        # Enter Hashtag and initial date
print("Enter Twitter HashTag to search for")
words = input()
print("Enter Date since The Tweets are required in yyyy-mm--dd")
date_since =input()

# number of tweets you want to extract in one run
numtweet = 2000
scrape(words, date_since, numtweet)

     