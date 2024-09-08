from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('todo/delete/<int:task_id>/', views.task_delete, name='task_delete'),
]