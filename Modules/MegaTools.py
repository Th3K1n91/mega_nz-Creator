import threading
from typing import Optional

from xitroo import Xitroo
from subprocess import run, PIPE
from Modules.Utils import *

class MegaTools:
    def __init__(self, email: str, password: str, threadLock: Optional[threading.Lock]):
        self.email = email
        self.password = password
        self.xitroo = Xitroo(email)
        self.info = get_inofs()
        self.lock = threadLock

        if os.name == 'nt':
            self.runnable = 'megatools.exe'
        elif os.name == 'posix':
            self.runnable = 'megatools'

        try:
            run(self.runnable, stdout=PIPE)
        except:
            if os.name == 'nt':
                print("megatools.exe not found")
            else:
                print('megatools binary not found\nDownload megatools to your path')

    def register(self):
        print('Registering '+self.email + "...")
        registerCMD: str = run([self.runnable,
                   "reg",
                   "--scripted",
                   "--register",
                   "--email", self.email,
                   "--name", self.info['Name'],
                   "--password", self.password],
                  stdout=PIPE).stdout.decode('utf-8').strip()
        otpLink: str = self.xitroo.waitForLatestMail().getBodyHtml().split('xml:lang="en">')[1].split('</a>')[0]

        verifyCMD: list = [self.runnable]
        verifyCMD.extend(registerCMD.replace('@LINK@', otpLink).split(" ")[1:])

        verify: str = run(verifyCMD, stdout=PIPE).stdout.decode('utf-8').strip()
        print(self.email+" "+verify)
        self.save()

    def save(self):
        if self.lock is not None:
            with self.lock:
                open("accounts.txt", "a").write(self.email + ":" + self.password + "\n")
        else:
            open("accounts.txt", "a").write(self.email + ":" + self.password + "\n")