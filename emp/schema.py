import strawberry
from typing import List, Optional
# 1. 앱 이름을 포함한 명확한 임포트 경로 사용
from emp.models import EmployeeModel

# 2. strawberry-django를 사용해 모델과 연결
@strawberry.django.type(EmployeeModel)
class Employee:
    id: strawberry.ID
    name: strawberry.auto
    age: strawberry.auto
    job: strawberry.auto
    language: strawberry.auto
    pay: strawberry.auto

@strawberry.input
class EmployeeInput:
    name: str
    age: int
    job: str
    language: str
    pay: int

@strawberry.type
class Query:
    # 3. resolver 함수에는 데코레이터 괄호()를 붙이는 것이 안전함
    @strawberry.field()
    def employees(self) -> List[Employee]:
        return EmployeeModel.objects.all()

@strawberry.type
class Mutation:
    @strawberry.mutation()
    def create_employee(self, input: EmployeeInput) -> Employee:
        return EmployeeModel.objects.create(**input.__dict__)

    @strawberry.mutation()
    def update_employee(self, id: strawberry.ID, input: EmployeeInput) -> Employee:
        employee = EmployeeModel.objects.get(id=id)
        for key, val in input.__dict__.items():
            setattr(employee, key, val)
        employee.save()
        return employee

    # 4. 반환 타입을 Django 모델이 아닌 Strawberry 타입(Employee)으로 지정
    @strawberry.mutation()
    def delete_employee(self, id: strawberry.ID) -> Employee:
        employee = EmployeeModel.objects.get(id=id)
        # 삭제 전 데이터를 보관했다가 정보를 반환
        employee_data = employee
        employee.delete()
        return employee_data