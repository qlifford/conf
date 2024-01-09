from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm, BlogUpdateForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blogapp/blog-create.html'
    success_url = reverse_lazy('blogs')

class BlogView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blogapp/blog-index.html'
    ordering = ['-created']

class BlogDetail(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blogapp/blog-detail.html'


class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    template_name = 'blogapp/blog-update.html'
    success_url = reverse_lazy('blogs')

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blogapp/blog-delete.html'
    success_url = reverse_lazy('blogs')