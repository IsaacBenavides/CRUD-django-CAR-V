from statistics import mode
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm


class IndexView(ListView):
    model = Blog
    queryset = Blog.objects.all()
    template_name = 'list_view.html'
    context_object_name = 'post_list'


class AddView(CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'add_view.html'
    success_url = '/'


class UpdateItemView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'update_view.html'
    success_url = '/'


class DeleteItemView(DeleteView):
    model = Blog
    template_name = 'delete_view.html'
    success_url = '/'
