from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Signal

from ui.base_ui.ui_auth_window import Ui_AuthWindow

from config import Messages
from utils import save_credentials

class AuthWindow(QMainWindow):
    auth_success_signal = Signal(str)

    def __init__(self, app):
        super(AuthWindow, self).__init__()
        self.ui = Ui_AuthWindow()
        self.ui.setupUi(self)

        self.ui.button_auth.clicked.connect(self.auth)

        self.app = app

    def auth(self):
        login = self.ui.line_edit_login.text()
        password = self.ui.line_edit_pass.text()

        if not login:
            QMessageBox.warning(self, 'Ошибка', Messages.LOGIN_IS_EMPTY)
            return

        if not password:
            QMessageBox.warning(self, 'Ошибка', Messages.PASSWORD_IS_EMPTY)
            return
 
        result = self.app.db_manager.find_employee(login)
        if not result:
            QMessageBox.warning(self, 'Ошибка', Messages.EMPLOYEE_DOES_NOT_EXIST)
            return

        result = self.app.db_manager.check_employee_password(login, password)
        if not result:
            QMessageBox.warning(self, 'Ошибка', Messages.WRONG_EMPLOYEE_PASSWORD)
            return
        else:
            if self.ui.radio_button_remember_me.isChecked():
                save_credentials(login, password)
            self.auth_success_signal.emit(result)