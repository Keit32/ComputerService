import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from db_manager import DBManager

if __name__ == "__main__":
    app = QApplication()
    db_manager = DBManager()

    window = MainWindow(app, db_manager)
    window.show()
    sys.exit(app.exec())