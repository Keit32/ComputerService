import hashlib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Dict, List, Any

from db_manager import DBManager
from config import Queries

app = FastAPI()
db_manager = DBManager()

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    name: str
    birth_date: str
    email: str
    password: str

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode('utf-8')).hexdigest()

@app.get("/get_data", response_model=Dict[str, List[Dict[str, Any]]])
def get_data():
    employees = db_manager.get_table_data("SELECT E.name, P.name, E.gender, E.birth_date, E.phone_number FROM employees E INNER JOIN positions P ON E.position = P.id;")
    records = db_manager.get_table_data("SELECT R.date, E.name, S.name, C.name, R.status FROM records R INNER JOIN employees E ON R.employee = E.id INNER JOIN services S ON R.service = S.id INNER JOIN clients C ON R.client = C.id;")
    
    try:
        employees_data = [dict(row) for row in employees] if employees else []
        records_data = [dict(row) for row in records] if records else []
    except Exception as e:
        print(e)
        raise HTTPException(404, "Data not found")

    data = {
        "employees": employees_data,
        "records": records_data
    }

    return data

@app.post("/login_client")
def login_client(login_request: LoginRequest):
    user = db_manager.get_table_data(Queries.LOGIN_CLIENT, (login_request.email,))[0]

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь с данной электронной почтой не зарегистрирован!")
    
    if user["password"] != hash_password(login_request.password):
        raise HTTPException(status_code=401, detail="Введён неверный пароль!")
    
    return {"id": user["id"], "name": user["name"]}

@app.post("/register_client")
def register_client(register_request: RegisterRequest):
    user = db_manager.get_table_data("SELECT id FROM clients WHERE email=?;", (register_request.email,))

    if user:
        raise HTTPException(status_code=400, detail="Пользователь с данной электронной почтой уже существует!")
    
    date_obj = datetime.fromisoformat(register_request.birth_date)
    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    db_manager.insert_table_data(Queries.ADD_CLIENT, (register_request.name, formatted_date, register_request.email, register_request.password))
    
    return {"message": "Пользователь успешно добавлен!"}