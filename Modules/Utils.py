import json
import os
import random
import string

def gen_accounts(prefix:str, domain: str = "@xitroo.de", count: int = 50) -> list:
    accounts: list = []
    for i in range(0, count):
        midlle: str = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(random.randint(4, 8)))
        accounts.append(prefix + midlle + domain)
    return accounts

def get_inofs():
    # firstnames = json.load(open('names.json'))["data"]
    # lastnames = json.load(open('lname.json'))["data"]
    firstnames = json.load(open(os.path.join(os.path.abspath(os.curdir), "Modules", "names.json")))["data"]
    lastnames = json.load(open(os.path.join(os.path.abspath(os.curdir), "Modules", "lname.json")))["data"]

    return {
        "Name": random.choice(firstnames) + " " + random.choice(lastnames),
    }