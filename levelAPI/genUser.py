import json
import requests as rq


def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load url")


def load_json(data):
    if not data is None:
        j = json.loads(data)
        return [j["results"][0]["name"]["first"], j["results"][0]["name"]["last"], j["results"][0]["email"]]


url = "https://randomuser.me/api"
values = load_json(get_data(url))
if values:
    print("First Name : %s\nLast Name : %s\nEmail is : %s" %(values[0], values[1], values[2]))












