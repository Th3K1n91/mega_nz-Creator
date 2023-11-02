#!/usr/bin/python3
#5.3.3
import queue, sys, time, os, threading, platform
pck = ["unofficial-xitroo-api==0.7", "pyqt5", "importlib_metadata"]
try:
    from subprocess import PIPE, run
    from importlib_metadata import version
    from PyQt5 import QtWidgets, QtGui, uic
    from Modules import gen, infos
    from xitroo.api import xitroo
except:
    os.system(f"pip3 install {' '.join(pck).strip()}")
    print("\nPlease Restart the bot")
    print("\nif you are on Linux and this step is repeated each time you launch it")
    print("\nor if you have an error while installing pyqt5")
    print("\nbe sure to install qt5 and python3-pyqt5")
    print("\nif this still does not work you will need to compile a more recent version of python 3")
    print("\nbe careful to use make altinstall so as not to replace the main version of your system")
    time.sleep(5)
    exit()

plt = platform.system()
if plt == "Linux" or plt == "Darwin":
    from pathlib import Path
    path_to_file = '/usr/bin/megatools'
    path = Path(path_to_file)
    if path.is_file():
        os.system("rm -f megatools.exe")
    else:
        print(f'please install megatools binary to /usr/bin folder')
        time.sleep(5)
        exit()


class Ui(QtWidgets.QDialog):
    def __init__(self):
        self.special_characters = "!@#$%^&*()[]{}-+?_=,<>/"
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.setWindowTitle("Mega.nz Creator")
        self.show()
        self.Image.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.start.clicked.connect(self.st)
        self.Name.mousePressEvent = self.pr
        self.Image.mousePressEvent = self.pr
        self.Github.mousePressEvent = self.gt

    def gt(self, event):
        self.urlOpenerUnix("https://github.com/Th3K1n91/mega_nz-Creator")

    def pr(self, event):
        self.urlOpenerUnix("https://cracked.io/insuckablyat88")

    def urlOpenerUnix(self, url):
        match plt:
            case "Windows":   os.system("start " + url)
            case "Linux":     os.system("x-www-browser " + url)
            case "Darwin":    os.system("safari " + url)

    def st(self):
        if self.username.text() and self.count.text() and self.password.text() and self.threads.text() != "":
            if len(self.password.text()) >= 8:
                if (any(char.isupper() for char in self.password.text()) and any(char.islower() for char in self.password.text())) and (any(char.isdigit() for char in self.password.text()) or any(char in self.special_characters for char in self.password.text())):
                    print("Please Wait")
                    accs = gen.gen_mega(f=str(self.username.text()).strip(), count=int(self.count.text())).gen_accounts()
                    set_pass = str(self.password.text())
                    for i in accs: q.put(i)
                    while q.empty() != True:
                        for i in range(int(self.threads.text())):
                            if q.empty(): continue
                            t = threading.Thread(target=megabot(e=q.get(), p=set_pass, l=self.DebugMode.isChecked()).start, args=())
                            threads.append(t)
                            t.start()
                        for t in threads: t.join()

class megabot:
    def __init__(self, e, p, l):
        #Vars
        self.mmail = e
        self.psw = p
        self.info = infos.get_inofs()
        self.log = l

    def start(self):
        try:
            r = run(f"megatools reg --register --email {self.mmail} --name {self.info['Name']} --password {self.psw}", stdout=PIPE)
            k = str(r.stdout).split("--verify ")[1].split(" ")[0]
            l = self.emailotp()
            c = run(f"megatools reg --verify {k} {l}", stdout=PIPE)
            if self.log:
                print(f"{r.stdout.decode('UTF-8')}\n{k}\n{l}\n{c.stdout.decode('UTF-8')}\n{c.stdout.decode('UTF-8')}")
            print(f"[{self.mmail}]\t{c.stdout.decode('UTF-8').split('!')[0]}")
            self.save_to()
        except Exception as e:
            if self.log:
                print(e)
            print("Error")
        except:
            print("Error")

    def emailotp(self):
        time.sleep(3)
        try: return "https://mega.nz/#confirm" + xitroo(self.mmail).get_bodyHtml().split("https://mega.nz/#confirm")[1].split('"')[0]
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
