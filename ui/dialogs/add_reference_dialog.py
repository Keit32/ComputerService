from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
)


class DynamicInputDialog(QDialog):
    def __init__(self, fields, name):
        super().__init__()
        self.setWindowTitle(f"Введите данные для нового объекта справочника '{name}'")
        self.fields = fields
        self.inputs = {}

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.form_layout = QFormLayout()
        for field in self.fields:
            input_field = QLineEdit()
            self.inputs[field["key"]] = input_field
            if field.get("password", False):
                input_field.setEchoMode(QLineEdit.Password)
            self.form_layout.addRow(field["label"], input_field)

        # Добавляем форму в основной макет
        self.layout.addLayout(self.form_layout)

        # Кнопки
        self.button_layout = QHBoxLayout()
        self.ok_button = QPushButton("Ок")
        self.cancel_button = QPushButton("Отмена")

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.cancel_button)
        self.layout.addLayout(self.button_layout)

    def get_data(self):
        """
        Возвращает данные из всех полей.

        :return: Словарь с данными.
        """
        return {key: input_field.text() for key, input_field in self.inputs.items()}


if __name__ == "__main__":
    app = QApplication([])

    # Пример 1: Диалог для сотрудников
    employee_fields = [
        {"key": "id", "label": "ID"},
        {"key": "name", "label": "ФИО"},
        {"key": "position", "label": "Должность"},
        {"key": "gender", "label": "Пол"},
        {"key": "birth_date", "label": "Дата рождения"},
        {"key": "phone_number", "label": "Номер телефона"},
        {"key": "login", "label": "Логин"},
        {"key": "password", "label": "Пароль", "password": True},
    ]

    # Пример 2: Диалог для должностей
    position_fields = [
        {"key": "id", "label": "ID"},
        {"key": "name", "label": "Наименование"},
    ]

    # Показываем диалог для сотрудников
    dialog = DynamicInputDialog(employee_fields, title="Данные сотрудника")
    if dialog.exec() == QDialog.Accepted:
        data = dialog.get_data()
        QMessageBox.information(None, "Данные сотрудника", str(data))

    # Показываем диалог для должностей
    dialog = DynamicInputDialog(position_fields, title="Данные должности")
    if dialog.exec() == QDialog.Accepted:
        data = dialog.get_data()
        QMessageBox.information(None, "Данные должности", str(data))

    app.exec()
