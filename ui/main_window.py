import sys

from PySide6.QtWidgets import QMainWindow

from ui.base_ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    
    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)