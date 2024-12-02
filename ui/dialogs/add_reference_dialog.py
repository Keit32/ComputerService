from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QComboBox, QDateEdit
from PySide6.QtCore import QDate

class AddDialog(QDialog):
    def __init__(self, fields, title="Введите данные"):
        super().__init__()
        self.setWindowTitle(title)
        self.fields = fields
        self.inputs = {}

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.form_layout = QFormLayout()
        for field in self.fields:
            if field["key"] == "id":
                continue

            widget = self.create_widget(field)
            self.inputs[field["key"]] = widget
            self.form_layout.addRow(field["label"], widget)

        self.layout.addLayout(self.form_layout)

        self.button_layout = QHBoxLayout()
        self.ok_button = QPushButton("Ок")
        self.cancel_button = QPushButton("Отмена")

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)
        self.layout.addLayout(self.button_layout)

    def create_widget(self, field):
        field_type = field.get("type")
        match field_type:
            case "lineedit":
                widget = QLineEdit()
                if field.get("key") == "password":
                    widget.setEchoMode(QLineEdit.Password)
            case "dateedit":
                widget = QDateEdit()
                widget.setCalendarPopup(True)
                widget.setDate(QDate.currentDate())
            case "combobox":
                widget = QComboBox()

                for option in field.get("options", {}):
                    widget.addItem(option[1], option[0])      
            case _:
                raise ValueError(f"Неизвестный тип виджета: {field_type}")
        return widget

    def get_data(self):
        data = {}
        for key, widget in self.inputs.items():
            if isinstance(widget, QLineEdit):
                data[key] = widget.text()
            elif isinstance(widget, QDateEdit):
                data[key] = widget.date().toString("yyyy-MM-dd") + " 00:00:00"
            elif isinstance(widget, QComboBox):
                data[key] = widget.currentData()
        return data