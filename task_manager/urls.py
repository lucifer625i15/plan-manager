from django.urls import path
from . import views
urlpatterns = [
    path('', views.task_list, name="task_list"),
    path('Create-task/', views.create_task, name="create_task"),
    path('update-task/', views.task_update, name="update-task/"),
    path('delete-task/<int:id>', views.task_delete, name="delete-task/"),
]