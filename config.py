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
    NOT_ENOUGH_RIGHTS = "Недостаточно прав для данного действия!"

@dataclass(frozen=True)
class Queries:
    FIND_EMPLOYEE = "SELECT id FROM employees WHERE login=?;"
    CHECK_EMPLOYEE_PASSWORD_QUERY = "SELECT id, name FROM employees WHERE login=? AND password = md5(?);"