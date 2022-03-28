import json


def retweetCount(dict):
    return dict['retweetCount']


def retweeted():
    top10 = []
    for tweet in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        read_tweet = json.loads(tweet)
        if len(top10) < 10:
            top10.append(read_tweet)
            top10.sort(reverse=True, key=retweetCount)
        elif read_tweet['retweetCount'] >= top10[9]['retweetCount']:
            top10.pop(9)
            top10.append(read_tweet)
            top10.sort(reverse=True, key=retweetCount)
    return top10
