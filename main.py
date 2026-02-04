import strawberry
from typing import List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Emp:
    id: str
    name: str
    age: int
    job: str
    language: str
    pay: int

@strawberry.input
class EmpInput:
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


@strawberry.type
class Query:

    @strawberry.field
    def employees(self) -> List[Emp]:
        return Employees

@strawberry.type
class Mutation:

    @strawberry.mutation
    def createEmployee(self, input: EmpInput) -> Emp:
        global Employees
        new_emp = Emp(
            id = str(max(int(item.id) for item in Employees) + 1) if Employees else "1",
            name = input.name,
            age = int(input.age),
            job = input.job,
            language = input.language,
            pay = int(input.pay),
        )
        Employees = [*Employees, new_emp]
        return new_emp

    @strawberry.mutation
    def updateEmployee(self, id: strawberry.ID,  input: EmpInput) -> Emp:
        global Employees
        new_emp = next((item for item in Employees if item.id==id), None)
        new_emp.name = input.name
        new_emp.age = int(input.age)
        new_emp.job = input.job
        new_emp.language = input.language
        new_emp.pay = int(input.pay)
        return new_emp

    @strawberry.mutation
    def deleteEmployee(self, id: strawberry.ID) -> strawberry.ID:
        global Employees
        Employees = [ item for item in Employees if item.id!=id ]
        return id

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


schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema=schema)
app.include_router(graphql_app, prefix="/graphql")



