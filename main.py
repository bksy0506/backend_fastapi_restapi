import os
from typing import List
from dotenv import load_dotenv

import strawberry
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base



load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()



class EmployeeModel(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    job = Column(String(50), nullable=False)
    language = Column(String(50), nullable=False)
    pay = Column(Integer, nullable=False)



@strawberry.type
class EmployeeType:
    id: strawberry.ID
    name: str
    age: int
    job: str
    language: str
    pay: int


@strawberry.input
class EmployeeInput:
    name: str
    age: int
    job: str
    language: str
    pay: int



def to_employee_type(e: EmployeeModel) -> EmployeeType:
    return EmployeeType(
        id=e.id,
        name=e.name,
        age=e.age,
        job=e.job,
        language=e.language,
        pay=e.pay,
    )

@strawberry.type
class Query:
    @strawberry.field
    def employees(self) -> List[EmployeeType]:
        with SessionLocal() as session:
            employees = session.query(EmployeeModel).all()
            print(employees)
            return [ to_employee_type(e) for e in employees]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createEmployee(self, input: EmployeeInput) -> EmployeeType:
        with SessionLocal() as session:
            employee = EmployeeModel(**input.__dict__)
            session.add(employee)
            session.commit()
            session.refresh(employee)
            return EmployeeType(employee)

    @strawberry.mutation
    def updateEmployee(
            self,
            id: strawberry.ID,
            input: EmployeeInput
    ) -> EmployeeType:
        with SessionLocal() as session:
            employee = (
                session.query(EmployeeModel)
                .filter(EmployeeModel.id == int(id))
                .first()
            )

            if not employee:
                raise HTTPException(status_code=404, detail="Employee not found")

            for key, value in input.__dict__.items():
                setattr(employee, key, value)

            session.commit()
            session.refresh(employee)
            return EmployeeType(employee)

    @strawberry.mutation
    def deleteEmployee(self, id: strawberry.ID) -> bool:
        with SessionLocal() as session:
            employee = (
                session.query(EmployeeModel)
                .filter(EmployeeModel.id == int(id))
                .first()
            )

            if not employee:
                raise HTTPException(status_code=404, detail="Employee not found")

            session.delete(employee)
            session.commit()
            return True

schema = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQLRouter(schema)
app = FastAPI()

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

app.include_router(graphql_app, prefix="/graphql")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)