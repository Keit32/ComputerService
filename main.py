import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.auth_window import AuthWindow
from db_manager import DBManager

class App:
    def __init__(self):
        self.app = QApplication()
        self.db_manager = DBManager()
        self.window = None
        self.show_window(AuthWindow)

    def show_window(self, window_class):
        if self.window:
            self.window.close()
        
        self.window = window_class(self)
        self.window.show()

    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = App()
    app.run()