import random
import requests

def get_inofs():
    firstnames = requests.get("https://www.randomlists.com/data/names-first.json").json()["data"]
    lastnames = requests.get("https://www.randomlists.com/data/names-surnames.json").json()["data"]

    return {
        "Name": random.choice(firstnames) + " " + random.choice(lastnames),
    }