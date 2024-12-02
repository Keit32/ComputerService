# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_auth_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        if not AuthWindow.objectName():
            AuthWindow.setObjectName(u"AuthWindow")
        AuthWindow.resize(600, 500)
        AuthWindow.setStyleSheet(u"#centralwidget {\n"
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
        self.centralwidget = QWidget(AuthWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(100, 50, 100, 50)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(48)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 41, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(-1, 0, -1, 20)
        self.label_login = QLabel(self.centralwidget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"font-size: 20px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_login)

        self.line_edit_login = QLineEdit(self.centralwidget)
        self.line_edit_login.setObjectName(u"line_edit_login")
        self.line_edit_login.setMinimumSize(QSize(200, 50))
        self.line_edit_login.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	border: 1px solid #fff;\n"
"	border-radius: 25px;\n"
"	padding: 0 10px;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	background-color: rgba(68, 68, 68, 200);\n"
"border-color:  rgba(255, 85, 255, 200);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_edit_login)

        self.label_pass = QLabel(self.centralwidget)
        self.label_pass.setObjectName(u"label_pass")
        self.label_pass.setStyleSheet(u"font-size: 20px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_pass)

        self.line_edit_pass = QLineEdit(self.centralwidget)
        self.line_edit_pass.setObjectName(u"line_edit_pass")
        self.line_edit_pass.setMinimumSize(QSize(0, 50))
        self.line_edit_pass.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	border: 1px solid #fff;\n"
"	border-radius: 25px;\n"
"	padding: 0 10px;\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	background-color: rgba(68, 68, 68, 200);\n"
"border-color:  rgba(255, 85, 255, 200);\n"
"}")
        self.line_edit_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.line_edit_pass)


        self.verticalLayout.addLayout(self.formLayout)

        self.radio_button_remember_me = QRadioButton(self.centralwidget)
        self.radio_button_remember_me.setObjectName(u"radio_button_remember_me")
        self.radio_button_remember_me.setStyleSheet(u"QRadioButton {\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"	width: 14px;\n"
"	height: 14px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"	width: 14px;\n"
"	height: 14px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 5px;\n"
"	background-color: rgba(255, 85, 255, 150);\n"
"}")

        self.verticalLayout.addWidget(self.radio_button_remember_me)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_auth = QPushButton(self.centralwidget)
        self.button_auth.setObjectName(u"button_auth")
        self.button_auth.setMinimumSize(QSize(0, 50))
        self.button_auth.setMaximumSize(QSize(200, 16777215))
        self.button_auth.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	font-size: 20px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}")

        self.horizontalLayout.addWidget(self.button_auth)


        self.verticalLayout.addLayout(self.horizontalLayout)

        AuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWindow)

        QMetaObject.connectSlotsByName(AuthWindow)
    # setupUi

    def retranslateUi(self, AuthWindow):
        AuthWindow.setWindowTitle(QCoreApplication.translate("AuthWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("AuthWindow", u"\u0412\u0445\u043e\u0434", None))
        self.label_login.setText(QCoreApplication.translate("AuthWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_pass.setText(QCoreApplication.translate("AuthWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.radio_button_remember_me.setText(QCoreApplication.translate("AuthWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.button_auth.setText(QCoreApplication.translate("AuthWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

