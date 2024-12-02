from dataclasses import dataclass

DEFAULT_DB_NAME = "PCService.db"

@dataclass(frozen=True)
class Messages:
    LOGIN_IS_EMPTY = "Для входа введите логин!"
    PASSWORD_IS_EMPTY = "Для входа введите пароль!"
    WRONG_EMPLOYEE_PASSWORD = "Неправильный пароль!"
    EMPLOYEE_DOES_NOT_EXIST = "Сотрудника с данным логином не существует!"
    EMPLOYEE_ALREADY_EXISTS = "Сотрудник с данным логином уже существует!"

@dataclass(frozen=True)
class Queries:
    GET_ALL_EMPLOYEES_QUERY = "SELECT * FROM employees;"
    FIND_EMPLOYEE = "SELECT id FROM employees WHERE login=?;"
    CHECK_EMPLOYEE_PASSWORD_QUERY = "SELECT * FROM employees WHERE login=? AND password = md5(?);"
    ADD_EMPLOYEE_QUERY = "INSERT INTO employees (name, position, gender, birth_date, phone_number, login, password) VALUES (?, ?, ?, ?, ?, ?, md5(?));"
    ADD_POSITION_QUERY = "INSERT INTO positions (name) VALUES (?);"