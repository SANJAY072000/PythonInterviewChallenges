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
        return j["results"][0]["name"]["first"]


url = "https://randomuser.me/api"
values = load_json(get_data(url))










