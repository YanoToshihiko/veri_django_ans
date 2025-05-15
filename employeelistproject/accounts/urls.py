from django.urls import path
from .views import login_view, logout_view, LogoutSuccessView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('logoutdone/', LogoutSuccessView.as_view(), name="logout-success"),
]
