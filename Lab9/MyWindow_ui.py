# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MyWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.action = QPushButton(self.centralwidget)
        self.action.setObjectName(u"action")
        self.action.setGeometry(QRect(160, 290, 141, 71))
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(360, 290, 141, 71))
        self.Result = QLabel(self.centralwidget)
        self.Result.setObjectName(u"Result")
        self.Result.setGeometry(QRect(570, 190, 121, 91))
        self.num1 = QLineEdit(self.centralwidget)
        self.num1.setObjectName(u"num1")
        self.num1.setGeometry(QRect(170, 140, 131, 71))
        self.num2 = QLineEdit(self.centralwidget)
        self.num2.setObjectName(u"num2")
        self.num2.setGeometry(QRect(370, 140, 131, 71))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.Result.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

