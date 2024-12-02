import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.auth_window import AuthWindow
from db_manager import DBManager

from utils import load_credentials, clear_credentials

class App:
    def __init__(self):
        self.app = QApplication()
        self.db_manager = DBManager()
        self.window = None

        credentials = load_credentials()
        
        if credentials:
            result = self.db_manager.check_employee_password(*credentials)
            if result:
                self.show_window(MainWindow)
                return
            else:
                clear_credentials()
        
        self.show_window(AuthWindow, self.setup_auth_window)

    def show_window(self, window_class, setup_callback=None):
        if self.window:
            self.window.close()
        
        self.window = window_class(self)

        if setup_callback:
            setup_callback()

        self.window.show()

    def setup_auth_window(self):
        self.window.auth_success_signal.connect(lambda: self.show_window(MainWindow))

    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = App()
    app.run()