#!/usr/bin/env python
import sys
import tweepy
import time
import csv

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

csvFile = open('result.csv', 'a')
csvWriter = csv.writer(csvFile)
maxid = 0

c = tweepy.Cursor(api.search,
                           q="#ukraine",
                           count=100,
                           result_type="mixed",
                           include_entities=False,
                           lang="en").items()
firsttweet = c.next()
maxid = firsttweet.id
print("max id is %d" % maxid)

while True:
    try:
        tweet = c.next()
        csvWriter.writerow([tweet.created_at, tweet.id, tweet.text.encode('utf-8'), tweet.coordinates, tweet.user.location.encode('utf-8'), tweet.user.screen_name.encode('utf-8')])
    except tweepy.TweepError:
        time.sleep(60 * 15)
        continue
    except StopIteration:
        break

while True:
    time.sleep(60 * 60)
    new_cursor = tweepy.Cursor(api.search,
                               q="#ukraine",
                               count=100,
                               result_type="mixed",
                               include_entities=False,
                               lang="en",
                               max_id=maxid).items()
    ftweet = new_cursor.next()
    maxid = ftweet.id
    while True:
        try:
            tweet = new_cursor.next()
            csvWriter.writerow([tweet.created_at, tweet.id, tweet.text.encode('utf-8'), tweet.coordinates, tweet.user.location.encode('utf-8'), tweet.user.screen_name.encode('utf-8')])
        except tweepy.TweepError:
            time.sleep(60 * 15)
            continue
        except StopIteration:
            break

csvFile.close()

