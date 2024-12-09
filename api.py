import hashlib
from fastapi import FastAPI, HTTPException, Query
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

class RecordRequest(BaseModel):
    date: str
    employee_name: str
    employee_birth_date: str
    service: str
    client_email: str
    status: str

def hash_password(password: str) -> str:
    return hashlib.md5(password.encode('utf-8')).hexdigest()

@app.get("/get_data", response_model=Dict[str, List[Dict[str, Any]]])
def get_data(email: str = Query(...)):
    employees = db_manager.get_table_data("SELECT E.name, P.name, E.gender, E.birth_date, E.phone_number FROM employees E INNER JOIN positions P ON E.position = P.id;")
    records = db_manager.get_table_data("SELECT R.date, E.name employee, S.name service, R.status FROM records R INNER JOIN clients C ON R.client = C.id INNER JOIN employees E ON R.employee = E.id INNER JOIN services S ON R.service = S.id WHERE C.email = ?", (email,))
    services = db_manager.get_table_data("SELECT S.name, S.price, TMU.name time_measurement_unit, S.duration FROM services S INNER JOIN time_measurement_units TMU ON S.time_measurement_unit = TMU.id;")

    try:
        employees_data = [dict(row) for row in employees] if employees else []
        records_data = [dict(row) for row in records] if records else []
        services_data = [dict(row) for row in services] if services else []
    except Exception as e:
        print(e)
        raise HTTPException(404, "Data not found")

    data = {
        "employees": employees_data,
        "records": records_data,
        "services": services_data
    }

    return data

@app.post("/login_client")
def login_client(login_request: LoginRequest):
    user = db_manager.get_table_data(Queries.LOGIN_CLIENT, (login_request.email,))

    if not user:
        raise HTTPException(status_code=404, detail="Пользователь с данной электронной почтой не зарегистрирован!")
    else:
        user = user[0]
    
    if user["password"] != hash_password(login_request.password):
        raise HTTPException(status_code=401, detail="Введён неверный пароль!")
    
    return {"id": user["id"], "name": user["name"]}

@app.post("/register_client")
def register_client(register_request: RegisterRequest):
    user = db_manager.get_table_data("SELECT id FROM clients WHERE email=?;", (register_request.email,))

    if user:
        raise HTTPException(status_code=400, detail="Пользователь с данной электронной почтой уже существует!")
    else:
        user = user[0]
    
    date_obj = datetime.fromisoformat(register_request.birth_date)
    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    db_manager.insert_table_data(Queries.ADD_CLIENT, (register_request.name, formatted_date, register_request.email, register_request.password))
    
    return {"message": "Пользователь успешно добавлен!"}

@app.post("/add_record")
def add_record(record_request: RecordRequest):

    date_obj = datetime.fromisoformat(record_request.date)
    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    date_obj = datetime.fromisoformat(record_request.employee_birth_date)
    formatted_employee_birth_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    employee = db_manager.get_table_data("SELECT id FROM employees WHERE name=? AND birth_date=?;", (record_request.employee_name, formatted_employee_birth_date))

    if employee:
        employee_id = employee[0][0]
    else:
        raise HTTPException(status_code=400, detail="Сотрудника с таким ФИО и датой рождения не существует!")
    
    service = db_manager.get_table_data("SELECT id FROM services WHERE name=?;", (record_request.service,))

    if service:
        service_id = service[0][0]
    else:
        raise HTTPException(status_code=400, detail="Услуги с таким наименованием не существует!")
    
    client = db_manager.get_table_data("SELECT id FROM clients WHERE email=?;", (record_request.client_email,))

    if client:
        client_id = client[0][0]
    else:
        raise HTTPException(status_code=400, detail="Клиента с такой электронной почтой не существует!")
    
    db_manager.insert_table_data(Queries.ADD_RECORD, (formatted_date, employee_id, service_id, client_id, record_request.status))
    
    return {"message": "Запись успешно добавлна!"}