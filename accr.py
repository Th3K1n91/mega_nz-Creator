import queue, sys, time, os, threading, requests
from subprocess import PIPE, run
from threading import Thread
xitroo_ver = requests.get("https://raw.githubusercontent.com/Th3K1n91/xitroo_api/main/version.txt").text.strip()
pck = ["unofficial-xitroo-api=="+xitroo_ver, "requests", "pyqt5", "importlib_metadata"]
try:
    from importlib_metadata import version
    from PyQt5 import QtWidgets, QtGui, uic
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtWidgets import QDialog
    from Modules.gen import gen_mega
    from Modules.infos import get_inofs
    if version('unofficial-xitroo-api') < xitroo_ver: os.system(f"pip install {pck[0]}")
    from xitroo.api import xitroo
except:
    os.system(f"pip install {' '.join(pck).strip()}")
    print("\nPlease Restart the bot")
    time.sleep(5)
    exit()

class Ui(QDialog):
    def __init__(self):
        self.special_characters = "!@#$%^&*()[]{}-+?_=,<>/"
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.setWindowTitle("Mega.nz Creator")
        self.show()
        self.image.setPixmap(QPixmap("images/logo.png"))
        self.start.clicked.connect(self.st)
        self.site.clicked.connect(self.pr)

    def pr(self):
        os.system("start https://cracked.io/insuckablyat88")

    def st(self):
        if self.username.text() and self.count.text() and self.password.text() and self.threads.text() != "":
            if len(self.password.text()) >= 8:
                if (any(char.isupper() for char in self.password.text()) and any(char.islower() for char in self.password.text())) and (any(char.isdigit() for char in self.password.text()) or any(char in self.special_characters for char in self.password.text())):
                    print("Please Wait")
                    accs = gen_mega(f=str(self.username.text()).strip(), count=int(self.count.text())).gen_accounts()
                    set_pass = str(self.password.text())
                    thread = int(self.threads.text())
                    for i in accs: q.put(i)
                    while True:
                        for i in range(thread):
                            t = Thread(target=megabot(e=q.get(), p=set_pass).start, args=())
                            threads.append(t)
                            t.start()
                        if q.empty() == True: break
                        for t in threads: t.join()

class megabot:
    def __init__(self, e, p):
        #Vars
        self.mmail = e
        self.psw = p
        self.info = get_inofs()

    def start(self):
        try:
            r = run(f"megatools reg --register --email {self.mmail} --name {self.info['Name']} --password {self.psw}", stdout=PIPE)
            k = str(r.stdout).split("--verify ")[1].split(" ")[0]
            l = self.emailotp()
            c = run(f"megatools reg --verify {k} {l}", stdout=PIPE)
            print(f"[{self.mmail}]\t{c.stdout.decode('UTF-8').split('!')[0]}")
            self.save_to()
        except: print("Error")

    def emailotp(self):
        time.sleep(2)
        try:
            emailtext = xitroo(self.mmail).get_bodyText()
            return emailtext.split('bestätigen:')[1].split('Mit')[0].replace('\n', '')
        except: return

    def save_to(self):
        lock.acquire()
        open("accounts.txt", "a+").write(f'{self.mmail}:{self.psw}\n')
        lock.release()

if __name__ == '__main__':
    # Vars
    lock = threading.Lock()
    q = queue.Queue()
    threads = list()
    # Start App
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()