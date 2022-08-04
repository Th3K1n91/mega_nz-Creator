xitroo_ver = "0.5"
pck = ["unofficial-xitroo-api=="+xitroo_ver, "selenium", "requests", "pyqt5", "undetected-chromedriver", "importlib_metadata"]
import queue, sys, time, os, threading, subprocess
from threading import Thread
try:
    import undetected_chromedriver as uc
    from importlib_metadata import version
    from PyQt5 import QtWidgets, QtGui, uic
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtWidgets import QDialog
    from Modules.gen import gen_mega
    from Modules.infos import get_inofs
    if version('unofficial-xitroo-api') < xitroo_ver: os.system(f"pip install {pck[0]}")
    from xitroo.api import xitroo
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except:
    os.system(f"pip install {' '.join(pck)}")
    print("\nPlease Restart the bot")
    time.sleep(5)
    exit()

class Ui(QDialog):
    def __init__(self):
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
        self.wait = 2
        self.psw = p
        self.vers = self.version()
        # DRIVER ------------------------------------------------------------------------------------------------
        self.options = uc.ChromeOptions()
        self.options.add_argument('--lang=de-DE')
        self.options.add_argument("--window-size=600,500")
        self.options.add_argument("--app=https://mega.nz/register")

    def start(self):
        retry = False
        self.driver = uc.Chrome(options=self.options, version_main=self.vers)
        while True:
            try:
                self.info = get_inofs()
                time.sleep(0.5)
                if retry == True:
                    try:
                        self.find('//*[@id="bodyel"]/section[5]/div[14]/button').click()
                        self.find('//*[@id="msgDialog"]/footer/div/div/button[2]').click()
                    except: pass
                self.register()
                self.driver.get(self.emailotp())
                self.confirm()
                time.sleep(2)
                break
            except:
                print("start class error\nRetrying")
                retry = True
        self.save_to()
        self.driver.close()

    def register(self):
        try:
            self.wai('//*[@id="register-firstname-registerpage2"]')
            self.find('//*[@id="register-firstname-registerpage2"]').send_keys(self.info["Name"].split()[0])
            self.find('//*[@id="register-lastname-registerpage2"]').send_keys(self.info["Name"].split()[1])
            self.find('//*[@id="register-email-registerpage2"]').send_keys(self.mmail)
            self.find('//*[@id="register-password-registerpage2"]').click()
            self.find('//*[@id="register-password-registerpage2"]').send_keys(self.psw)
            self.find('//*[@id="register-password-registerpage3"]').click()
            self.find('//*[@id="register-password-registerpage3"]').send_keys(self.psw)
            self.find('//*[@id="register_form"]/div[8]/div[1]/input').click()
            self.find('//*[@id="register-check-registerpage2"]').click()
            self.find('//*[@id="register_form"]/button').click()
        except:
            print('Register ERROR')
            return

    def emailotp(self):
        time.sleep(5)
        try:
            emailtext = xitroo(self.mmail).get_bodyText()
            return emailtext.split('bestätigen:')[1].split('Mit')[0].replace('\n', '')
        except: return

    def confirm(self):
        self.find('//*[@id="login-password2"]').click()
        self.find('//*[@id="login-password2"]').send_keys(self.psw)
        self.find('//*[@id="login_form"]/button').click()

    def save_to(self):
        lock.acquire()
        open("accounts.txt", "a+").write(f'{self.mmail}:{self.psw}\n')
        lock.release()

    # SOME ASSETS ------------------------------------------------------------------------------------------------
    def wai(self, xpath): WebDriverWait(self.driver, 600).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find(self, xpath):
        time.sleep(self.wait)
        return self.driver.find_element(By.XPATH, xpath)
    # Get Chrome version for line:69
    def version(self):
        try:
            out = subprocess.Popen(
                ['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'],
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).communicate()
            return int(out[0].decode('UTF-8').strip().split()[-1].split(".")[0])
        except:
            print("Install Chrome")
            input("Press Enter to Close Programm")
            exit()

if __name__ == '__main__':
    # Vars
    lock = threading.Lock()
    q = queue.Queue()
    threads = list()
    # Start App
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
