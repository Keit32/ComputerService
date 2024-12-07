from dataclasses import dataclass

DEFAULT_DB_NAME = "PCService.db"

RESTRICT_EDIT_LIST = ["Сотрудники"]

@dataclass(frozen=True)
class Messages:
    LOGIN_IS_EMPTY = "Для входа введите логин!"
    PASSWORD_IS_EMPTY = "Для входа введите пароль!"
    WRONG_EMPLOYEE_PASSWORD = "Неправильный пароль!"
    EMPLOYEE_DOES_NOT_EXIST = "Сотрудника с данным логином не существует!"
    EMPLOYEE_ALREADY_EXISTS = "Сотрудник с данным логином уже существует!"
    REFERENCE_OBJECT_ADDED_SUCCESSFUL = "Новый объект справочника {0} был успешно добавлен!"
    REFERENCE_OBJECT_ADD_FAILED = "Не удалось добавить новый объект справочника {0}!"
    REFERENCE_OBJECT_EDITED_SUCCESSFUL = "Объект справочника {0} был успешно изменён!"
    REFERENCE_OBJECT_EDIT_FAILED = "Не удалось изменить объект справочника {0}!"
    REFERENCE_OBJECT_DELETED_SUCCESSFUL = "Объект справочника {0} был успешно удалён!"
    REFERENCE_OBJECT_DELETE_FAILED = "Не удалось удалить объект справочника {0}!"
    DOCUMENT_OBJECT_ADDED_SUCCESSFUL = "Новый объект документа {0} был успешно добавлен!"
    DOCUMENT_OBJECT_ADD_FAILED = "Не удалось добавить новый объект документа {0}!"
    DOCUMENT_OBJECT_EDITED_SUCCESSFUL = "Объект документа {0} был успешно изменён!"
    DOCUMENT_OBJECT_EDIT_FAILED = "Не удалось изменить объект документа {0}!"
    DOCUMENT_OBJECT_DELETED_SUCCESSFUL = "Объект документа {0} был успешно удалён!"
    DOCUMENT_OBJECT_DELETE_FAILED = "Не удалось удалить объект документа {0}!"
    NOT_ENOUGH_RIGHTS = "Недостаточно прав для данного действия!"

@dataclass(frozen=True)
class Queries:
    FIND_EMPLOYEE = "SELECT id FROM employees WHERE login=?;"
    CHECK_EMPLOYEE_PASSWORD_QUERY = "SELECT id, name FROM employees WHERE login=? AND password = md5(?);"