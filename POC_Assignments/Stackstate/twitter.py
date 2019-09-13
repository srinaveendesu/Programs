# stdlib
import sys
import time
from hashlib import md5

# 3rd party
import tweepy

# project
from checks import AgentCheck


class TWITTERCheck(AgentCheck):
    def check(self, instance):
        mandatory_req = ['client_key', 'client_secret',
                         'access_key', 'access_secret']
        flag = False
        for key in mandatory_req:
            if key not in instance.keys():
                flag = True
        if flag:
            print("Keys not given.")
            self.log.error("Keys not given.")
            return
        client_key = instance['client_key']
        client_secret = instance['client_secret']
        access_key = instance['access_key']
        access_secret = instance['access_secret']
        auth = tweepy.OAuthHandler(client_key, client_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)
        if (not api):
            print("Can't Authenticate")
            self.log.error("Can't Authenticate")
            return
        screen_name = instance['screen_name']
        aggregation_key = md5('test').hexdigest()
        if instance['test'] == 'twitter_metrics':
            tweets = self.get_mention_tweets(api, screen_name)
            checked = []
            for tweet in tweets:
                print(tweet.text.encode('utf-8'))
                if tweet.text not in checked:
                    self.count(tweet.text.encode("utf-8"))
                    checked.append(tweet.text)
                else:
                    self.increment(tweet.text)
        elif instance['test'] == 'twitter_events':
            tweets = self.get_tweets(api, screen_name)
            data = ''
            for tweet in tweets:
                # If need to create seperate event for every
                # tweet
                # self.twitter_post_event(tweet.text, tweet.id,
                #        aggregation_key)
                data = data + tweet.text
            self.twitter_post_event(tweet.text, len(tweets), aggregation_key)

    def get_tweets(self, api, screen_name):
        new_tweets = api.user_timeline(screen_name=screen_name, count=10)
        return new_tweets

    def twitter_post_event(self, tweet, tweet_id, aggregation_key):
        self.event({
            'timestamp': int(time.time()),
            'event_type': 'Twitter',
            'msg_title': 'Tweet ID  %s' % tweet_id,
            'msg_text': 'Tweet Message %s' % (tweet),
            'aggregation_key': aggregation_key
                        })

    def get_mention_tweets(self, api, screen_name):
        searchQuery = screen_name
        maxTweets = 10000000
        tweetsPerQry = 100
        sinceId = None
        max_id = -1
        tweetCount = 0
        messages = []

        print("Downloading max {0} tweets".format(maxTweets))
        self.log.debug("Downloading max {0} tweets".format(maxTweets))

        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry)
                    else:
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry,
                                                since_id=sinceId)
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=searchQuery,
                                                count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
                if not new_tweets:
                    print("No more tweets found")
                    self.log.debug("No more tweets found")
                    break
                for tweet in new_tweets:
                    messages.append(tweet)
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                self.log.debug("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                self.log.error("some error : " + str(e))
                break

        return messages


if __name__ == '__main__':
    check, instances = TWITTERCheck.from_yaml('/path/to/conf.d/http.yaml')
    for instance in instances:
        print "\nRunning the check against tests: %s" % (instance['test'])
        check.check(instance)
        if check.has_events():
            print 'Events: %s' % (check.get_events())
        print 'Metrics: %s' % (check.get_metrics())