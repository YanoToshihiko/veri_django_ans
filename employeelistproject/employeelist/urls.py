from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.ListEmployeeView.as_view(), name="list-employee"),
    path("employee/create/", views.CreateEmployeeView.as_view(), name="create-employee"),
]
