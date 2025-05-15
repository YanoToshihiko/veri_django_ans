from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.ListEmployeeView.as_view(), name="list-employee"),
    path("employee/create/", views.CreateEmployeeView.as_view(), name="create-employee"),
    path("employee/<int:pk>/detail/", views.DetailEmployeeView.as_view(), name="detail-employee"),
    path("employee/<int:pk>/update/", views.UpdateEmployeeView.as_view(), name="update-employee"),
    path("employee/<int:pk>/delete/", views.DeleteEmployeeView.as_view(), name="delete-employee"),
    path("employee/contact", views.contact_view, name="contact-employee"),
]
