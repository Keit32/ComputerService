import json

from PySide6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Signal

from ui.base_ui.ui_main_window import Ui_MainWindow
from ui.dialogs.reference_dialog import ReferenceDialog

from config import Messages, RESTRICT_EDIT_LIST
from models.reference import Reference

class MainWindow(QMainWindow):
    log_out_signal = Signal()

    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.app = app

        self.references = []

        self.current_reference = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_log_out.clicked.connect(self.log_out)
        self.ui.add_reference_row_button.clicked.connect(self.add_reference)
        self.ui.references_list.currentItemChanged.connect(lambda: self.load_table(self.ui.selected_reference_table))

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
            
    def load_table(self, table):
        for reference in self.references:
            if reference.name == self.ui.references_list.currentItem().text():
                self.current_reference = reference
                break

        data = self.app.db_manager.get_table_data(self.current_reference.get_data_query)
        if not data:
            self.ui.selected_reference_table.setRowCount(0)
            self.ui.selected_reference_table.setColumnCount(0)
            return

        headers_fields = [field["label"] for field in self.current_reference.fields]
        
        try:
            password_field_index = headers_fields.index('Пароль')
        except ValueError:
            password_field_index = None
        
        if password_field_index:
            headers_fields.pop(password_field_index)

        headers = headers_fields

        self.ui.selected_reference_table.setRowCount(len(data))
        self.ui.selected_reference_table.setColumnCount(len(headers))
        self.ui.selected_reference_table.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                header_item = self.ui.selected_reference_table.horizontalHeaderItem(col_idx).text()

                self.ui.selected_reference_table.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

        self.ui.selected_reference_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.selected_reference_table.resizeColumnsToContents()

    def load_data(self):
        self.load_references_data()

    def load_references_data(self):
        with open("data/reference.json", "r", encoding="utf8") as f:
            references_data = json.load(f)
        
        for reference_data in references_data:
            reference_name = reference_data.get("name")
            reference_sql_table_name = reference_data.get("sql_table_name")
            reference_get_data_query = reference_data.get("get_data_query")
            reference_insert_data_query = reference_data.get("insert_data_query")
            reference_fields = reference_data.get("fields")
            self.references.append(Reference(reference_name, reference_sql_table_name, reference_fields, reference_get_data_query, reference_insert_data_query))

        for reference in self.references:
            for field in reference.fields:
                options_sql_table = field.get("options_sql_table", None)
                if not options_sql_table:
                    continue
                
                for reference in self.references:
                    if reference.sql_table_name == options_sql_table:
                        field["options"] = [(field[0], field[1]) for field in self.app.db_manager.get_table_data(reference.get_data_query)]
                        continue

    def load_lists(self):
        for reference in self.references:
            self.ui.references_list.addItem(reference.name)

    def add_reference(self):
        if not self.current_reference:
            return
        
        if self.current_reference.name in RESTRICT_EDIT_LIST and not self.app.db_manager.is_admin:
            QMessageBox.warning(self, "Ошибка", Messages.NOT_ENOUGH_RIGHTS)
            return

        dialog = ReferenceDialog(self.current_reference.fields, self.current_reference.name)
        if dialog.exec() == QDialog.Accepted:
            data = list(dialog.get_data().values())
            if self.app.db_manager.insert_table_data(self.current_reference.insert_data_query, data):
                QMessageBox.information(self, "Успешно", Messages.REFERENCE_OBJECT_ADDED_SUCCESSFUL.format((self.current_reference.name)))
                self.load_table(self.ui.selected_reference_table)
            else:
                QMessageBox.warning(self, "Ошибка", Messages.REFERENCE_OBJECT_ADD_FAILED.format((self.current_reference.name)))

<<<<<<< HEAD
    def edit_reference(self):
        selected_row = self.ui.selected_reference_table.currentRow()
        if selected_row == -1:
            return
        
        if self.current_reference.name in RESTRICT_EDIT_LIST and not self.app.db_manager.is_admin:
            QMessageBox.warning(self, "Ошибка", Messages.NOT_ENOUGH_RIGHTS)
            return
        
        current_object = [self.ui.selected_reference_table.item(selected_row, column).text() for column in range(self.ui.selected_reference_table.columnCount())]
        current_object_id = current_object[0]
        current_object = current_object[1:]

        dialog = ReferenceDialog(self.current_reference.fields, self.current_reference.name, current_object)
        if dialog.exec() == QDialog.Accepted:
            data = list(dialog.get_data().values())

    def delete_reference(self):
        selected_row = self.ui.selected_reference_table.currentRow()
        if selected_row == -1:
            return
        
        if self.current_reference.name in RESTRICT_EDIT_LIST and not self.app.db_manager.is_admin:
            QMessageBox.warning(self, "Ошибка", Messages.NOT_ENOUGH_RIGHTS)
            return

        dialog = QMessageBox()
        dialog.setWindowTitle("Подтверждение")
        dialog.setText("Вы уверены, что хотите удалить данную строку?")
        dialog.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        result = dialog.exec()
        
        if result == QMessageBox.Ok:
            if self.app.db_manager.delete_table_data(self.current_reference.delete_data_query, current_object_id):
                QMessageBox.information(self, "Успешно", Messages.REFERENCE_OBJECT_DELETED_SUCCESSFUL)
                self.load_table(self.ui.selected_reference_table)
            else:
                QMessageBox.warning(self, "Ошибка", Messages.REFERENCE_OBJECT_DELETE_FAILED)

=======
>>>>>>> parent of 39eb14a (Completely working delete object from reference)
    def log_out(self):
        self.log_out_signal.emit()