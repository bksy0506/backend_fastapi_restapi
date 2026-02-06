import strawberry
from emp.schema import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)