from db_connection import DBConnection, QueryAction

from config import Queries

class DBManager:
    def __init__(self):
        self.db = DBConnection()
        self.user_id = None
        self.user_name = None
        self.is_admin = False

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
            self.user_name = user[1]
            if self.user_id == 1:
                self.is_admin = True

            return True

    def get_table_data(self, query, args=()):
        return self.db.execute_query(query, action=QueryAction.FETCHALL, args=args)
    
    def get_table_data_by_id(self, query, id):
        return self.db.execute_query(query, (id,), action=QueryAction.FETCHONE)
    
    def insert_table_data(self, query, args):
        return self.db.execute_query(query, args)
    
    def update_table_data(self, query, args):
        return self.db.execute_query(query, args)
    
    def delete_table_data(self, query, id):
        return self.db.execute_query(query, (id,))