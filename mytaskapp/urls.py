from django.urls import path
from . import views
urlpatterns = [
    path('login_page/', views.login_page, name = 'login_page'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout_page, name = 'logout'),

    path('task_view/', views.task_view, name = 'task_view'),
    path('task_update/<str:id>/', views.task_update, name = 'task_update'),
    path('task_delete/<str:id>/', views.task_delete, name = 'task_delete'),
]