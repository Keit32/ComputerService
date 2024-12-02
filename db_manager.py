from db_connection import DBConnection, QueryAction

from config import Queries

class DBManager:
    def __init__(self):
        self.db = DBConnection()
        self.user_id = None
        self.admin = False

    def find_employee(self, login):
        user = self.db.execute_query(Queries.FIND_EMPLOYEE, (login,), action=QueryAction.FETCHONE)
        if not user:
            return False
        else:
            return True
        
    def check_employee_password(self, login, password):
        user = self.db.execute_query(Queries.CHECK_EMPLOYEE_PASSWORD_QUERY, (login, password), action=QueryAction.FETCHONE)
        if not user:
            return False
        else:
            self.user_id = user[0]
            if self.user_id == 1:
                self.admin = True

            return True

    def get_all_users(self):
        print(self.db.execute_query(Queries.GET_ALL_EMPLOYEES_QUERY, action=QueryAction.FETCHALL))

    def add_user(self, name, position, gender, birth_date, phone_number, login, password):
        self.db.execute_query(Queries.ADD_EMPLOYEE_QUERY, (name, position, gender, birth_date, phone_number, login, password))
    
    def add_position(self, name):
        self.db.execute_query(Queries.ADD_POSITION_QUERY, (name,))