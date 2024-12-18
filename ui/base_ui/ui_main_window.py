# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.welcome_employee = QLabel(self.centralwidget)
        self.welcome_employee.setObjectName(u"welcome_employee")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(18)
        font.setBold(True)
        self.welcome_employee.setFont(font)
        self.welcome_employee.setStyleSheet(u"")
        self.welcome_employee.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.welcome_employee)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_log_out = QPushButton(self.centralwidget)
        self.button_log_out.setObjectName(u"button_log_out")
        self.button_log_out.setMinimumSize(QSize(150, 50))
        self.button_log_out.setMaximumSize(QSize(16777215, 16777215))
        self.button_log_out.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.button_log_out)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabs = QTabWidget(self.centralwidget)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setStyleSheet(u"QWidget {\n"
"background-color: #333;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background-color: #333;\n"
"  padding: 5px;\n"
"  font-size: 18px;\n"
"  border: 1px solid #444;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"   background-color: #444;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"   background-color: #555;\n"
"}")
        self.references_tab = QWidget()
        self.references_tab.setObjectName(u"references_tab")
        self.verticalLayout_2 = QVBoxLayout(self.references_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.references_list = QListWidget(self.references_tab)
        self.references_list.setObjectName(u"references_list")
        self.references_list.setMaximumSize(QSize(300, 16777215))
        font1 = QFont()
        font1.setPointSize(14)
        self.references_list.setFont(font1)
        self.references_list.setStyleSheet(u"QListWidget::item {\n"
"	padding: 5px 0;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(85, 85, 85);\n"
"}")

        self.horizontalLayout_2.addWidget(self.references_list)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, -1, 10)
        self.add_reference_row_button = QPushButton(self.references_tab)
        self.add_reference_row_button.setObjectName(u"add_reference_row_button")
        self.add_reference_row_button.setMinimumSize(QSize(120, 40))
        self.add_reference_row_button.setMaximumSize(QSize(16777215, 16777215))
        self.add_reference_row_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	font-size: 20px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}")

        self.horizontalLayout_3.addWidget(self.add_reference_row_button)

        self.edit_reference_row_button = QPushButton(self.references_tab)
        self.edit_reference_row_button.setObjectName(u"edit_reference_row_button")
        self.edit_reference_row_button.setMinimumSize(QSize(120, 40))
        self.edit_reference_row_button.setMaximumSize(QSize(16777215, 16777215))
        self.edit_reference_row_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	font-size: 20px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}")

        self.horizontalLayout_3.addWidget(self.edit_reference_row_button)

        self.delete_reference_row__button = QPushButton(self.references_tab)
        self.delete_reference_row__button.setObjectName(u"delete_reference_row__button")
        self.delete_reference_row__button.setMinimumSize(QSize(120, 40))
        self.delete_reference_row__button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	font-size: 20px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}")

        self.horizontalLayout_3.addWidget(self.delete_reference_row__button)

        self.spacerr = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.spacerr)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.selected_reference_table = QTableWidget(self.references_tab)
        self.selected_reference_table.setObjectName(u"selected_reference_table")
        self.selected_reference_table.setStyleSheet(u"QTableWidget {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"font-size: 16px;\n"
"}\n"
"QTableCornerButton {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QTableCornerButton::section {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QHeaderView {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QHeaderView::section {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QComboBox {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"border: 1px solid rgba(255, 255, 255, .2);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover {\n"
"border: 1px solid rgba(255, 255, 255, .6);\n"
"}\n"
"QComboBox:focus {\n"
"border: 1px solid rgba(255, 255, 255, .8);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;\n"
"	padding: 5px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
""
                        "QScrollBar::handle:vertical {\n"
"	background-color: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"    width:20px;\n"
"    height:20px;\n"
"	border-radius: 10px;\n"
"    subcontrol-position: right top;\n"
"    subcontrol-origin:margin;\n"
"    border: 1px solid rgba(255, 255, 255, .2);\n"
"	background: transparent;\n"
"	image: url(\":/image/arrow-down.png\");\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"    border: 2px solid rgba(255, 255, 255, .6);\n"
"}\n"
"QScrollBar:vertical {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(85, 85, 85);\n"
"}\n"
"QScrollBar:horizontal {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(85, 85, 85);\n"
"}")

        self.verticalLayout_3.addWidget(self.selected_reference_table)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabs.addTab(self.references_tab, "")
        self.documents_tab = QWidget()
        self.documents_tab.setObjectName(u"documents_tab")
        self.layoutWidget = QWidget(self.documents_tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1161, 661))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.documemts_list = QListWidget(self.layoutWidget)
        self.documemts_list.setObjectName(u"documemts_list")
        self.documemts_list.setMaximumSize(QSize(300, 16777215))
        self.documemts_list.setFont(font1)
        self.documemts_list.setStyleSheet(u"QListWidget::item {\n"
"	padding: 5px 0;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(85, 85, 85);\n"
"}")

        self.horizontalLayout_4.addWidget(self.documemts_list)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 10, -1, 10)
        self.add_document_row_button = QPushButton(self.layoutWidget)
        self.add_document_row_button.setObjectName(u"add_document_row_button")
        self.add_document_row_button.setMinimumSize(QSize(120, 40))
        self.add_document_row_button.setMaximumSize(QSize(16777215, 16777215))
        self.add_document_row_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	font-size: 20px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}")

        self.horizontalLayout_5.addWidget(self.add_document_row_button)

        self.edit_document_row_button = QPushButton(self.layoutWidget)
        self.edit_document_row_button.setObjectName(u"edit_document_row_button")
        self.edit_document_row_button.setMinimumSize(QSize(120, 40))
        self.edit_document_row_button.setMaximumSize(QSize(16777215, 16777215))
        self.edit_document_row_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	font-size: 20px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}")

        self.horizontalLayout_5.addWidget(self.edit_document_row_button)

        self.delete_document_row__button = QPushButton(self.layoutWidget)
        self.delete_document_row__button.setObjectName(u"delete_document_row__button")
        self.delete_document_row__button.setMinimumSize(QSize(120, 40))
        self.delete_document_row__button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(68, 68, 68, 100);\n"
"	font-size: 20px;\n"
"	border: 1px solid #fff;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(68, 68, 68, 150);\n"
"	border-color:  rgba(255, 85, 255, 100);\n"
"}")

        self.horizontalLayout_5.addWidget(self.delete_document_row__button)

        self.spacerr_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.spacerr_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.selected_document_table = QTableWidget(self.layoutWidget)
        self.selected_document_table.setObjectName(u"selected_document_table")
        self.selected_document_table.setStyleSheet(u"QTableWidget {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"font-size: 16px;\n"
"}\n"
"QTableCornerButton {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QTableCornerButton::section {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QHeaderView {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QHeaderView::section {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"}\n"
"QComboBox {\n"
"background: none;\n"
"background-color: rgba(100, 100, 100, 50);\n"
"border: 1px solid rgba(255, 255, 255, .2);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover {\n"
"border: 1px solid rgba(255, 255, 255, .6);\n"
"}\n"
"QComboBox:focus {\n"
"border: 1px solid rgba(255, 255, 255, .8);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background: transparent;\n"
"	padding: 5px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
""
                        "QScrollBar::handle:vertical {\n"
"	background-color: rgb(85, 85, 85);\n"
"}\n"
"QComboBox::drop-down {\n"
"    width:20px;\n"
"    height:20px;\n"
"	border-radius: 10px;\n"
"    subcontrol-position: right top;\n"
"    subcontrol-origin:margin;\n"
"    border: 1px solid rgba(255, 255, 255, .2);\n"
"	background: transparent;\n"
"	image: url(\":/image/arrow-down.png\");\n"
"}\n"
"QComboBox::drop-down:hover {\n"
"    border: 2px solid rgba(255, 255, 255, .6);\n"
"}\n"
"QScrollBar:vertical {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background-color: rgb(85, 85, 85);\n"
"}\n"
"QScrollBar:horizontal {\n"
"	background: none;\n"
"	background-color: rgb(68, 68, 68);\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background-color: rgb(85, 85, 85);\n"
"}")

        self.verticalLayout_4.addWidget(self.selected_document_table)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.tabs.addTab(self.documents_tab, "")
        self.administration_tab = QWidget()
        self.administration_tab.setObjectName(u"administration_tab")
        self.administration_tab.setEnabled(True)
        self.tabs.addTab(self.administration_tab, "")

        self.verticalLayout.addWidget(self.tabs)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u044b\u0439 \u0441\u0435\u0440\u0432\u0438\u0441", None))
        self.welcome_employee.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c, <\u0424\u0418\u041e>!", None))
        self.button_log_out.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.add_reference_row_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit_reference_row_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delete_reference_row__button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabs.setTabText(self.tabs.indexOf(self.references_tab), QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a\u0438", None))
        self.add_document_row_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.edit_document_row_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.delete_document_row__button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.tabs.setTabText(self.tabs.indexOf(self.documents_tab), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.tabs.setTabText(self.tabs.indexOf(self.administration_tab), QCoreApplication.translate("MainWindow", u"\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

