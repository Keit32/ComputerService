# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"	\n"
"	background-color: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QWidget {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMessageBox {\n"
"	background-color: #444444;\n"
"}\n"
"\n"
"QMessageBox QPushButton {\n"
"	background-color: #666666;\n"
"	min-height: 30px;\n"
"	min-width: 80px;\n"
"	border: 1 px solid #ffffff;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"	background-color: #777777;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0439 \u0441\u0435\u0440\u0432\u0438\u0441", None))
    # retranslateUi

