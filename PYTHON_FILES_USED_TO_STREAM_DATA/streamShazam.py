from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'ajAxCxamgszW30C7xMU7Aw4m9'
consumer_secret = '3kDA9TlFVqT8QBaKng48Ng65MY7cIBty8medfZydhEL1wsDHrM'
access_token = '1103878713005924352-yaIEEWkuQbr9x2tEybk0QjeDoiVlKm'
access_token_secret = 'F6F8EpNg7uZhKdKaIrmmhlovNBSVAl083jeVLuj7vrJ5W'


class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Shazam", "shazam", "SHAZAM", "ShazamMovie", ], languages=["en"])
