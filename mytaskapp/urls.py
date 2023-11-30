from django.urls import path
from . import views
urlpatterns = [
    path('', views.task_view, name = 'task_view'),
    path('task_update/<str:id>/', views.task_update, name = 'task_update'),
    path('task_delete/<str:id>/', views.task_delete, name = 'task_delete'),
]