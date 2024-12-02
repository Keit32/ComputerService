import sys

from PySide6.QtWidgets import QMainWindow

from ui.base_ui.ui_main_window import Ui_MainWindow
from db_manager import DBManager

class MainWindow(QMainWindow):
    
    def __init__(self, app, db_manager: DBManager):
        super(MainWindow, self).__init__()

        self.app = app
        self.db_manager = db_manager

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def close_app(self):
        sys.exit()