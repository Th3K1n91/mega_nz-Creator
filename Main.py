import queue
import sys
import threading

import PySide6.QtCore

from Modules.Utils import *
from Modules.MegaTools import MegaTools
from Modules.Gui import Ui_MainWindow
from PySide6.QtCore import QThreadPool, Signal
from PySide6.QtWidgets import QMainWindow, QApplication

class Main(QMainWindow):
    running = Signal(bool)

    def __init__(self):
        self.threadmanager = QThreadPool()
        self.accountQueue = queue.Queue()
        self.runnable: str
        self.validPass: bool = False
        self.lock = threading.Lock()

        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.version.setText("V5.4.3")

        self.ui.password.textChanged.connect(self.checkPassword)
        self.running.connect(self._setUI)
        self.ui.start.clicked.connect(self.threadStart)
        self.ui.info.mousePressEvent = self.info
        self.ui.infogithub.mousePressEvent = self.github

    def worker(self, password, tid):
        while not self.accountQueue.empty():
            try:
                MegaTools(self.accountQueue.get(), password, self.lock).register()
            except Exception as e:
                print(f"Thread {tid} caught exception: {e}")

    def threadStart(self):
        threading.Thread(target=self.start).start()

    def start(self):
        inputs: list = [self.ui.password.text(), self.ui.username.text(), self.ui.threads.text(), self.ui.count.text()]
        empyt = any(len(sinput) == 0 for sinput in inputs)
        if self.validPass and not empyt:
            self.running.emit(True)
            accs: list = gen_accounts(prefix=self.ui.username.text(), count=int(self.ui.count.text()))
            password: str = self.ui.password.text()

            threads: list = []
            for acc in accs:
                self.accountQueue.put(acc)

            for i in range(0, int(self.ui.threads.text())):
                if not self.accountQueue.empty():
                    t = threading.Thread(target=self.worker, args=(password, i, ))
                    threads.append(t)
                    t.start()
            for t in threads:
                t.join()
            threads.clear()
            self.running.emit(False)

    def _setUI(self, boolean: bool):
        self.ui.start.setDisabled(boolean)
        self.ui.password.setDisabled(boolean)
        self.ui.username.setDisabled(boolean)
        self.ui.count.setDisabled(boolean)
        self.ui.threads.setDisabled(boolean)

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
