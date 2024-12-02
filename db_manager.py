from db_connection import DBConnection, QueryAction

GET_ALL_EMPLOYEES_QUERY = "SELECT * FROM employees;"
ADD_EMPLOYEE_QUERY = "INSERT INTO employees (name, position, gender, birth_date, phone_number, login, password) VALUES (?, ?, ?, ?, ?, ?, md5(?));"
ADD_POSITION_QUERY = "INSERT INTO positions (name) VALUES (?);"

class DBManager:
    def __init__(self):
        self.db = DBConnection()

    def get_all_users(self):
        print(self.db.execute_query(GET_ALL_EMPLOYEES_QUERY, action=QueryAction.FETCHALL))

    def add_user(self, name, position, gender, birth_date, phone_number, login, password):
        self.db.execute_query(ADD_EMPLOYEE_QUERY, (name, position, gender, birth_date, phone_number, login, password))
    
    def add_position(self, name):
        self.db.execute_query(ADD_POSITION_QUERY, (name,))