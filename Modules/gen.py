import random
import string


class gen_mega:
    def __init__(self, f, l="@xitroo.de", count=50):
        self.f = f
        self.l = l
        self.count = count

    def gen_accounts(self):
        accounts = list()
        for i in range(0, self.count):
            self.m = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(random.randint(4, 8)))
            accounts.append(str(self.f+self.m+self.l))
        return accounts