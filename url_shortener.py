import genkey
import db
import re

def genURL(data):
    url = data
    key = genkey.generateKey()
    db.insert(key, url)
    return ("localhost:8000/"+key)


def retURL(path):
    rankey = re.findall('\/(.*)', path)
    for i in rankey:
        rankey = i

    stourl = db.retrieve(rankey)
    return stourl

# print("New URL: sho.rt/"+key)
# url = db.retrieve(key)
# print(url)