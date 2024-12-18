from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QComboBox, QDateEdit, QDateTimeEdit
from PySide6.QtCore import QDate

class ItemDialog(QDialog):
    def __init__(self, fields, name, data=[]):
        super().__init__()
        self.setWindowTitle(f"Введите данные для объекта справочника \"{name}\"")
        self.fields = fields
        self.inputs = {}

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.form_layout = QFormLayout()
        for index, field in enumerate(self.fields):
            if field["key"] == "id":
                continue

            widget = self.create_widget(field, data, index-1)
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

    def create_widget(self, field, data, index):
        field_type = field.get("type")
        match field_type:
            case "lineedit":
                widget = QLineEdit()
                if field.get("key") == "password":
                    widget.setEchoMode(QLineEdit.Password)
                else:
                    if data:
                        widget.setText(data[index])
            case "dateedit":
                widget = QDateEdit()
                widget.setCalendarPopup(True)

                if data:
                    widget_date = QDate.fromString(data[index].split()[0], "yyyy-MM-dd")
                else:
                    widget_date = QDate.currentDate()

                widget.setDate(widget_date)
            case "datetimeedit":
                widget = QDateTimeEdit()
                widget.setCalendarPopup(True)

                if data:
                    widget_date = QDate.fromString(data[index].split()[0], "yyyy-MM-dd hh:mm:ss")
                else:
                    widget_date = QDate.currentDate()

                widget.setDate(widget_date)
            case "combobox":
                widget = QComboBox()

                for option in field.get("options", {}):
                    widget.addItem(option[1], option[0])  

                if data:
                    index = widget.findData(data[index])
                    widget.setCurrentIndex(index) 
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
            elif isinstance(widget, QDateTimeEdit):
                data[key] = widget.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            elif isinstance(widget, QComboBox):
                data[key] = widget.currentData()
        return data