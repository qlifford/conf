from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('', views.home_page, name = 'home-page'),

]