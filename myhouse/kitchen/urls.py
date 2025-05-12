from django.urls import path
from .views import KitchenView

urlpatterns = [
    path('', KitchenView.as_view(), name='kitchen-home'),
]

