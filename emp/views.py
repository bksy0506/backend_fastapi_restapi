from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import EmployeeModel
from .seriallizers import  EmployeeSerializer



class EmployeeListCreateAPIView(APIView):

     def get(self, request):
         employees = EmployeeModel.objects.all()
         serializer = EmployeeSerializer(employees, many=True)
         return Response(serializer.data)

     def post(self, request):
         print(request.data)
         serializer = EmployeeSerializer(data=request.data)
         print(serializer.is_valid())
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class EmployeeUpdateDeleteAPIView(APIView):
    def put(self, request, id):

        employee = EmployeeModel.objects.get(id=(id))

        if not employee:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee = EmployeeModel.objects.get(id=id)
        if not employee:
            return Response(status=status.HTTP_404_NOT_FOUND)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






