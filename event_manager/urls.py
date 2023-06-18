from django.urls import path
from . import views
urlpatterns = [
    path('', views.event_list, name="task_event"),
    path('create-event/', views.create_event, name="create_event"),
    path('update-event/<int:id>', views.event_update, name="update-event"),
    path('delete-event/<int:id>', views.event_delete, name="delete-event"),
]