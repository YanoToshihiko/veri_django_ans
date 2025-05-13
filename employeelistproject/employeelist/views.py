from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import Employee
from django.urls import reverse_lazy

# Create your views here.


class CreateEmployeeView(CreateView):
    template_name = "employeelist/create.html"
    model = Employee
    fields = ["no", "name", "salary"]
    success_url = reverse_lazy("list-employee")


class ListEmployeeView(ListView):
    template_name = "employeelist/list.html"
    model = Employee
