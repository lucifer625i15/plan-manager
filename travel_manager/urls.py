from django.urls import path
from . import views
urlpatterns = [
    path('', views.travel_list, name="travel_list"),
    path('create-travel/', views.create_travel, name="create_travel"),
    path('update-travel/<int:id>', views.travel_update, name="update-travel"),
    path('delete-travel/<int:id>', views.travel_delete, name="delete-travel"),
]