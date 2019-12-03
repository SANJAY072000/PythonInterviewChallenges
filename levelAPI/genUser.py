import json
import requests as rq


def get_data(url):
    try:
        return rq.get(url).text
    except Exception as e:
        print("Unable to load url")













