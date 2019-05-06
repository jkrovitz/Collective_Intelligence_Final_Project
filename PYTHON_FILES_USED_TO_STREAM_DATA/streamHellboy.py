from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = '----FILL IN----'
consumer_secret = '----FILL IN----'
access_token = '----FILL IN----'
access_token_secret = '----FILL IN----'


class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Hellboy", "#Hellboy", "HellboyMovie"], languages=["en"])
