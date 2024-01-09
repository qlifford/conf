from django.urls import path
from . import views
from blogapp.views import BlogView, BlogDetail, BlogCreate, BlogUpdate, BlogDelete
urlpatterns = [
    path('', BlogView.as_view(), name = 'blogs'),

    path('<str:pk>/detail', BlogDetail.as_view(), name = 'blog-detail'),
    path('<str:pk>/edit/', BlogUpdate.as_view(), name = 'blog-update'),
    path('blog-create/', BlogCreate.as_view(), name = 'blog-create'),
    path('<str:pk>/delete/', BlogDelete.as_view(), name = 'blog-delete'),
]