from fastapi import FastAPI, HTTPException
from db_manager import DBManager
from typing import List

if __name__ == "__main__":
    app = FastAPI()
    db_manager = DBManager()