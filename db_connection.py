import sqlite3
import hashlib
from enum import Enum

from config import DEFAULT_DB_NAME

HASHCODE_NAME = "md5"

class QueryType(Enum):
    SINGLE = 0
    MANY = 1
    SCRIPT = 2

class QueryAction(Enum):
    COMMIT = 0
    FETCHONE = 1
    FETCHMANY = 2
    FETCHALL = 3

class DBConnection:
    @staticmethod
    def md5sum(value):
        return hashlib.md5(value.encode('utf-8')).hexdigest()
    
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.user_id = None

    def execute_query(self, query, args=(), type=QueryType.SINGLE, action=QueryAction.COMMIT,
                      fetcharg=1):
        self.connect()
        self.conn.create_function(HASHCODE_NAME, 1, self.md5sum)
        try:
            match type:
                case QueryType.SINGLE:
                    self.cursor.execute(query, args)
                case QueryType.MANY:
                    self.cursor.executemany(query, args)
                case QueryType.SCRIPT:
                    self.cursor.executescript(query)
            match action:
                case QueryAction.COMMIT:
                    self.conn.commit()
                    return True
                case QueryAction.FETCHONE:
                    result = self.cursor.fetchone()
                    return result
                case QueryAction.FETCHMANY:
                    result = self.cursor.fetchmany(fetcharg)
                    return result
                case QueryAction.FETCHALL:
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
