from django.urls import path
from .views import goodbye

urlpatterns = [
    path('goodbye', goodbye),
]
