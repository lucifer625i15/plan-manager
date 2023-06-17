from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.register, name="register"),
]