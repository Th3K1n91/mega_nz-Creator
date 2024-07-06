import queue
import sys
import threading
from Modules.Utils import *
from Modules.MegaTools import MegaTools
from Modules.Gui import Ui_MainWindow
from PySide6.QtCore import QThreadPool
from PySide6.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow):
    def __init__(self):
        self.threadmanager = QThreadPool()
        self.runnable: str
        self.validPass: bool = False

        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.version.setText("V5.4.0")

        self.ui.password.textChanged.connect(self.checkPassword)

        self.ui.start.clicked.connect(self.startSafely)
        self.ui.info.mousePressEvent = self.info
        self.ui.infogithub.mousePressEvent = self.github

    def start(self):
        inputs: list = [self.ui.password.text(), self.ui.username.text(), self.ui.threads.text(), self.ui.count.text()]
        empyt = any(len(sinput) == 0 for sinput in inputs)
        if self.validPass and not empyt:
            self.ui.start.setDisabled(True)
            self.ui.password.setDisabled(True)
            self.ui.username.setDisabled(True)
            self.ui.count.setDisabled(True)
            self.ui.threads.setDisabled(True)

            accs: list = gen_accounts(prefix=self.ui.username.text(), count=int(self.ui.count.text()))
            password: str = self.ui.password.text()
            que = queue.Queue()
            threads: list = []
            for acc in accs:
                que.put(acc)

            while not que.empty():
                for i in range(0, int(self.ui.threads.text())):
                    if not que.empty():
                        t = threading.Thread(target=MegaTools(que.get(), password).register)
                        threads.append(t)
                        t.start()
                for t in threads:
                    threads.remove(t)
                    t.join()

            self.ui.start.setDisabled(False)
            self.ui.password.setDisabled(False)
            self.ui.username.setDisabled(False)
            self.ui.count.setDisabled(False)
            self.ui.threads.setDisabled(False)

    def startSafely(self):
        self.threadmanager.start(self.start)

    def openUrl(self, url):
        match os.name:
            case "nt": os.system("start " + url)
            case "posix": os.system("x-www-browser " + url)

    def info(self, event):
        self.openUrl("https://cracked.io/insuckablyat88")

    def github(self, event):
        self.openUrl("https://github.com/Th3K1n91/mega_nz-Creator")

    def checkPassword(self):
        special_characters = "!@#$%^&*()[]{}-+?_=,<>/"
        password = self.ui.password.text()

        hasSpecialChar = any(char in password for char in special_characters)
        hasDigit = any(char.isdigit() for char in password)
        hasUpper = any(char.isupper() for char in password)
        hasLower = any(char.islower() for char in password)
        hasNoSpace = not any(char.isspace() for char in password)
        hasLength = len(password) >= 8

        valid = lambda x: "QLabel#" + x + "{color:green;}"
        notValid = lambda x: "QLabel#" + x + "{color:rgb(192, 28, 40);}"

        if hasUpper and hasLower:
            self.ui.upperlower.setStyleSheet(valid("upperlower"))
        else:
            self.ui.upperlower.setStyleSheet(notValid("upperlower"))

        if hasSpecialChar or hasDigit:
            self.ui.special.setStyleSheet(valid("special"))
        else:
            self.ui.special.setStyleSheet(notValid("special"))

        if hasLength:
            self.ui.chars.setStyleSheet(valid("chars"))
        else:
            self.ui.chars.setStyleSheet(notValid("chars"))

        self.validPass = (hasSpecialChar or hasDigit) and hasUpper and hasNoSpace and hasLength




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main()
    window.show()

    sys.exit(app.exec())
