import json

from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal

from models.reference import Reference
from ui.base_ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    log_out_signal = Signal()

    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.app = app
        self.references = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_log_out.clicked.connect(self.log_out)

        self.ui.welcome_employee.setText(f"Добро пожаловать, {self.app.db_manager.user_name}!")
        if not self.app.db_manager.is_admin:
            self.remove_administration_tab()

        self.load_data()
        self.load_lists()

    def remove_administration_tab(self):
        for index in range(self.ui.tabs.count()):
            if self.ui.tabs.widget(index) == self.ui.administration_tab:
                self.ui.tabs.removeTab(index)
                return
            
    def load_data(self):
        self.load_references_data()

    def load_references_data(self):
        with open("data/reference.json", "r", encoding="utf8") as f:
            references_data = json.load(f)
        
        for reference_data in references_data:
            reference_name = reference_data.get("name")
            reference_sql_table_name = reference_data.get("sql_table_name")
            reference_fields = reference_data.get("fields")
            self.references.append(Reference(reference_name, reference_sql_table_name, reference_fields))

    def load_lists(self):
        for reference in self.references:
            self.ui.references_list.addItem(reference.name)
            
    def log_out(self):
        self.log_out_signal.emit()