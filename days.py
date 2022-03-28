import json
import re
from datetime import datetime


def date():
    top10 = {}
    lista = []
    lista_final = []
    for tweet in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        read_tweet = json.loads(tweet)

        cr_date = read_tweet['date']
        match = re.search(r'\d{4}-\d{2}-\d{2}', cr_date)
        date = datetime.strptime(match.group(), '%Y-%m-%d').date()

        if date in top10.keys():
            top10[date] += 1
        else:
            top10[date] = 1

    lista = sorted(top10.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 10):
        tupla = str(lista[i][0]), lista[i][1]
        lista_final.append(tupla)

    return lista_final
