from django.urls import path
from .views import LivingRoomView, WindowSideView

urlpatterns = [
    path('', LivingRoomView.as_view(), name='livingroom-home'),
    path('window/', WindowSideView.as_view(), name='window-side'),
]
