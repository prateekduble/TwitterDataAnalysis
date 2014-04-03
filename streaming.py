import tweepy
import json
import csv

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

csvFile = open('result.csv', 'a')
csvWriter = csv.writer(csvFile)

# This is the listener, resposible for rieceiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        csvWriter.writerow([decoded['created_at'], decoded['id'], decoded['text'].encode('utf-8'), decoded['coordinates'], decoded['user']['location'].encode('utf-8'), decoded['user']['screen_name'].encode('utf-8')])

        #print '@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'))
        #print ''
        return True

    def on_error(self, status):
        print('Got an error with status code: ' + str(status))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, l)
    stream.filter(track=['ukraine','crimea','russia'])
