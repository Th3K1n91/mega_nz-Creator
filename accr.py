pck = ["selenium", "requests", "pyqt5"]
import queue
import sys
import time
import install
import os
from threading import Thread
try:
    from PyQt5 import QtWidgets, QtGui,uic
    from PyQt5.QtGui import QPixmap
    from PyQt5.QtWidgets import QDialog
    from Modules.gen import gen_mega
    from Modules.infos import get_inofs
    from Modules.xitrooapi import xitroo
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
except:
    for p in pck:
        install.install(p)
    print("\nPlease Restart")
    time.sleep(5)


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
            print(1)
            accs = gen_mega(f=str(self.username.text()).strip(), count=int(self.count.text())).gen_accounts()
            set_pass = str(self.password.text())
            thread = int(self.threads.text())

            q = queue.Queue()
            threads = list()
            for i in accs:
                q.put(i)
            while True:
                for i in range(thread):
                    t = Thread(target=megabot(e=q.get(), p=set_pass).start, args=())
                    threads.append(t)
                    t.start()

                if q.empty() == True:
                    break

                for t in threads:
                    t.join()

class megabot:
    def __init__(self, e, p):
        self.mmail = e
        self.wait = 2
        self.psw = p
        # DRIVER ------------------------------------------------------------------------------------------------
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=de-DE')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        path = "driver\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=path, options=options)
        self.driver.set_window_size(1280, 720)

    def start(self):
        retry = False
        while True:
            try:
                self.info = get_inofs()
                time.sleep(2)
                self.driver.get('https://mega.nz/register')
                if retry == True:
                    try:
                        self.find('//*[@id="bodyel"]/section[5]/div[14]/button').click()
                        self.find('//*[@id="msgDialog"]/footer/div/div/button[2]').click()
                    except:
                        pass
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

    def emailotp(self):
        time.sleep(5)
        while True:
            try:
                emailtext = xitroo(self.mmail).get_bodytext()
                break
            except:
                pass
        try:
            return emailtext.decode("UTF-8").split('bestätigen:')[1].split('Mit')[0].replace('\n','')
        except:
            return False

    def confirm(self):
        self.find('//*[@id="login-password2"]').click()
        self.find('//*[@id="login-password2"]').send_keys(self.psw)
        self.find('//*[@id="login_form"]/button').click()

    def save_to(self):
        open("accounts.txt", "a+").write(f'{self.mmail}:{self.psw}\n')

    # SOME ASSETS ------------------------------------------------------------------------------------------------
    def wai(self, xpath):
        WebDriverWait(self.driver, 600).until(EC.visibility_of_element_located((
            By.XPATH, xpath)))

    def find(self, xpath):
        time.sleep(self.wait)
        return self.driver.find_element(By.XPATH, xpath)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()