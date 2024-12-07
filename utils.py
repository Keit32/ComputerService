from PySide6.QtCore import QSettings

def save_credentials(login, password):
    settings = QSettings("KeitProd", "ComputerService")
    settings.setValue("login", login)
    settings.setValue("password", password)

def load_credentials():
    settings = QSettings("KeitProd", "ComputerService")
    saved_login = settings.value("login", "")
    saved_password = settings.value("password", "")

    if saved_login and saved_password:
        return (saved_login, saved_password)
    else:
        return False

def clear_credentials():
    settings = QSettings("KeitProd", "ComputerService")
    settings.setValue("login", "")
    settings.setValue("password", "")