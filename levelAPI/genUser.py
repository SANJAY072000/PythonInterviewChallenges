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
        return [j["results"][0]["name"]["title"] + ". " + j["results"][0]["name"]["first"] + j["results"][0]["name"]["last"], j["results"][0]["email"], j["results"][0]["gender"], j["results"][0]["dob"]["date"]]


url = "https://randomuser.me/api"
values = load_json(get_data(url))
if values:
    print("Name : %s\nEmail : %s\nGender : %s\nDOB : %s" %(values[0], values[1], values[2], values[3].split('T')[0]))












