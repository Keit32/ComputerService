from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal

from ui.base_ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    log_out_signal = Signal()

    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.app = app

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_log_out.clicked.connect(self.log_out)

        self.ui.welcome_employee.setText(f"Добро пожаловать, {self.app.db_manager.user_name}!")
        if not self.app.db_manager.is_admin:
            self.remove_administration_tab()

    def remove_administration_tab(self):
        for index in range(self.ui.tabs.count()):
            if self.ui.tabs.widget(index) == self.ui.administration_tab:
                self.ui.tabs.removeTab(index)
                return
            
    def log_out(self):
        self.log_out_signal.emit()