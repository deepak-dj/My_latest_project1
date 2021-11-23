from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializer import Employee_serializer


class employee_data(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_serializer

