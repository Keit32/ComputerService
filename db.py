import sqlite3

from config import DEFAULT_DB_NAME

class DBConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.user_id = None

    def execute_query(self, query, args=(), type='single', action='commit',
                      fetcharg=1):
        self.connect()
        try:
            match type:
                case 'single':
                    self.cursor.execute(query, args)
                case 'many':
                    self.cursor.executemany(query, args)
                case 'script':
                    self.cursor.executescript(query)
            match action:
                case 'commit':
                    self.conn.commit()
                    return True
                case 'fetchone':
                    result = self.cursor.fetchone()
                    return result
                case 'fetchmany':
                    result = self.cursor.fetchmany(fetcharg)
                    return result
                case 'fetchall':
                    result = self.cursor.fetchall()
                    return result
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.close()

    def connect(self):
        try:
            if self.conn is None:
                self.conn = sqlite3.connect(DEFAULT_DB_NAME)
                self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
            raise

    def close(self):
        try:
            if self.conn is not None:
                self.cursor.close()
                self.conn.close()
                self.conn = None
                self.cursor = None
        except Exception as e:
            print(e)
            raise
