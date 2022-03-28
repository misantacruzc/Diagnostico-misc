import json
from re import T


def statusesCount(dict):
    return dict['statusesCount']


def users():
    top10 = {}
    lista = []
    for tweet in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        read_tweet = json.loads(tweet)
        if len(top10) < 10:
            if read_tweet['user']['username'] in top10.keys():
                if read_tweet['user']['statusesCount'] >= top10[read_tweet['user']['username']]:
                    top10[read_tweet['user']['username']] = read_tweet['user']['statusesCount']
            else:
                top10[read_tweet['user']['username']] = read_tweet['user']['statusesCount']
            lista = sorted(top10.items(), key=lambda x: x[1], reverse=True)

        else:
            if read_tweet['user']['username'] in top10.keys():
                if read_tweet['user']['statusesCount'] >= top10[read_tweet['user']['username']]:
                    top10[read_tweet['user']['username']] = read_tweet['user']['statusesCount']
            else:
                if read_tweet['user']['statusesCount'] >= lista[9][1]:
                    top10.pop(lista[9][0])
                    top10[read_tweet['user']['username']] = read_tweet['user']['statusesCount']
                    lista = sorted(top10.items(), key=lambda x: x[1], reverse=True)

    return lista
