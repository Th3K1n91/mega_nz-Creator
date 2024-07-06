# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'megaURgDuC.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(376, 415)
        icon = QIcon()
        icon.addFile(u"images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color:rgb(31, 31, 31)\n"
"}\n"
"QLabel {\n"
"	color: rgb(255, 255, 255)\n"
"}\n"
"QLineEdit {\n"
"	color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 1px solid white;\n"
"}\n"
"QLabel#upperlower, QLabel#chars, QLabel#special {\n"
"	color:rgb(192, 28, 40)\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(39, 42, 52);\n"
"}\n"
"QCheckBox, QPushButton {\n"
"	color: white;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 16777215))
        self.label_10.setFrameShape(QFrame.NoFrame)
        self.label_10.setFrameShadow(QFrame.Plain)
        self.label_10.setLineWidth(0)
        self.label_10.setMidLineWidth(0)
        self.label_10.setTextFormat(Qt.MarkdownText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setMargin(10)
        self.label_10.setIndent(-1)

        self.verticalLayout_2.addWidget(self.label_10)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(40, -1, 40, -1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.count = QLineEdit(self.centralwidget)
        self.count.setObjectName(u"count")

        self.horizontalLayout_4.addWidget(self.count)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.threads = QLineEdit(self.centralwidget)
        self.threads.setObjectName(u"threads")

        self.horizontalLayout_5.addWidget(self.threads)


        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")

        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.chars = QLabel(self.centralwidget)
        self.chars.setObjectName(u"chars")
        self.chars.setMinimumSize(QSize(0, 18))

        self.verticalLayout.addWidget(self.chars)

        self.special = QLabel(self.centralwidget)
        self.special.setObjectName(u"special")
        self.special.setMinimumSize(QSize(0, 18))

        self.verticalLayout.addWidget(self.special)

        self.upperlower = QLabel(self.centralwidget)
        self.upperlower.setObjectName(u"upperlower")
        self.upperlower.setMinimumSize(QSize(0, 18))

        self.verticalLayout.addWidget(self.upperlower)


        self.gridLayout.addLayout(self.verticalLayout, 2, 1, 1, 1)

        self.username = QLineEdit(self.centralwidget)
        self.username.setObjectName(u"username")

        self.gridLayout.addWidget(self.username, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(70, 70))
        self.label_7.setMaximumSize(QSize(70, 70))
        self.label_7.setBaseSize(QSize(0, 0))
        self.label_7.setPixmap(QPixmap(u"images/logo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setMargin(0)

        self.horizontalLayout.addWidget(self.label_7)

        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")
        self.info.setCursor(QCursor(Qt.PointingHandCursor))
        self.info.setStyleSheet(u"QLabel#info {\n"
"	border: 2px solid white;\n"
"	border-radius: 5px\n"
"}")
        self.info.setFrameShape(QFrame.NoFrame)
        self.info.setMidLineWidth(0)

        self.horizontalLayout.addWidget(self.info)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 2)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.start = QPushButton(self.centralwidget)
        self.start.setObjectName(u"start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy1)
        self.start.setMinimumSize(QSize(125, 46))
        self.start.setMaximumSize(QSize(125, 46))
        self.start.setSizeIncrement(QSize(0, 0))
        self.start.setBaseSize(QSize(0, 0))
        self.start.setCursor(QCursor(Qt.PointingHandCursor))
        self.start.setAutoFillBackground(False)
        self.start.setStyleSheet(u"QPushButton#start {\n"
"	background-color:rgb(31, 31, 31);\n"
"	border-radius: 5px;\n"
"	border: 2px solid white;\n"
"}\n"
"QPushButton#start:hover {\n"
"	color: rgb(31, 31, 31);\n"
"	background-color:white;\n"
"	border-radius: 5px;\n"
"	border: 2px solid white;\n"
"}")
        self.start.setCheckable(False)
        self.start.setAutoRepeat(False)

        self.horizontalLayout_3.addWidget(self.start)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.version = QLabel(self.centralwidget)
        self.version.setObjectName(u"version")

        self.horizontalLayout_2.addWidget(self.version)

        self.infogithub = QLabel(self.centralwidget)
        self.infogithub.setObjectName(u"infogithub")
        self.infogithub.setCursor(QCursor(Qt.PointingHandCursor))
        self.infogithub.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.infogithub)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mega Creator", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"# Mega.nz Creator", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Count:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Threads:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.chars.setText(QCoreApplication.translate("MainWindow", u"- 8 Characters", None))
        self.special.setText(QCoreApplication.translate("MainWindow", u"- 1 Digit/Special", None))
        self.upperlower.setText(QCoreApplication.translate("MainWindow", u"- Upper & Lower", None))
        self.username.setPlaceholderText("")
        self.label_7.setText("")
        self.info.setText(QCoreApplication.translate("MainWindow", u"By InSuckaBlyat88\n"
"Cracked.io/insuckablyat88", None))
        self.start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(shortcut)
        self.start.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.version.setText(QCoreApplication.translate("MainWindow", u"V0.0.0", None))
        self.infogithub.setText(QCoreApplication.translate("MainWindow", u"Github", None))
    # retranslateUi

