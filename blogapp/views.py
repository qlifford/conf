from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Blog

class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title','title_tag', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.date = self.request.date
        return super().form_valid(form)

class BlogView(ListView):
    model = Blog
    ordering = ['-created']

class BlogDetail(DetailView):
    model = Blog

class BlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title','title_tag', 'body']

class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')