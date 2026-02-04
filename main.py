from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Emp(BaseModel):
    id: str
    name: str
    age: int
    job: str
    language: str
    pay: int

class EmpInput(BaseModel):
    name: str
    age: int
    job: str
    language: str
    pay: int

Employees : List[Emp] = [
    Emp(id="1", name="John",  age=35, job="frontend",  language="react",      pay=400),
    Emp(id="2", name="Peter", age=28, job="backend",   language="java",       pay=300),
    Emp(id="3", name="Sue",   age=38, job="publisher", language="javascript", pay=400),
    Emp(id="4", name="Susan", age=45, job="pm",        language="python",     pay=500),
]

app = FastAPI(title="emp restapi")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/emp", response_model=List[Emp])
def get_employees():
    return Employees

@app.post("/emp", response_model=Emp, status_code=200)
def create_employee(input: EmpInput):
    global Employees
    new_emp = Emp(
        id = str(max([int(item.id) for item in Employees]) + 1) if Employees else "1",
        name = input.name,
        age = input.age,
        job = input.job,
        language = input.language,
        pay = input.pay,
    )
    Employees.append(new_emp)
    return new_emp

@app.put("/emp/{emp_id}", response_model=EmpInput, status_code=200)
def update_employee(emp_id: str, input: EmpInput):
    global Employees
    Employees = [
        Emp( id= emp_id,
             name= input.name,
             age= input.age,
             job= input.job,
             language = input.language,
             pay =  input.pay
    ) if item.id == emp_id else item for item in Employees
    ]

    return input

@app.delete("/emp/{emp_id}")
def delete_employee(emp_id: str):
    global Employees
    Employees = [ item for item in Employees if item.id != emp_id]
    return emp_id


