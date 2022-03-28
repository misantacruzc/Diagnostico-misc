import json
import re
from datetime import datetime


def hashtag():
    top10 = {}
    lista = []
    lista_final = []
    for tweet in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        read_tweet = json.loads(tweet)
        content = read_tweet['content']
        match = re.findall("#", content)
        if match:
            for i in match:
                hasht = re.search("#", content)
                if hasht:
                    start = hasht.start()
                else:
                    break

                contentleft = content[start:]
                espacio = re.search(" ", contentleft)
                salto = re.search("\n", contentleft)
                if espacio and salto:
                    if espacio.start() > salto.start():
                        end = salto.start()
                    else:
                        end = espacio.start()
                elif espacio:
                    end = espacio.start()
                elif salto:
                    end = salto.start()
                else:
                    end = len(content) - start
                if content[start:start+end][-1] == "." or content[start:start+end][-1] == ",":
                    end = end - 1
                hashtagfind = content[start:start+end]
                if hashtagfind in top10.keys():
                    top10[hashtagfind] += 1
                else:
                    top10[hashtagfind] = 1
                content = content[start+end:]
        match = []

    lista = sorted(top10.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 10):
        lista_final.append(lista[i])

    return lista_final
