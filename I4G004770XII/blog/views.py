from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "PostList.html"

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "postform.html"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    template_name = "postdetail.html"

class PostUpdateView(UpdateView):
    model = Postfields = "__all__"
    template_name = "PostList.html"
    success_url = reverse_lazy("blog:all")



class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    template_name = "postconfirmdelete.html"
    success_url = reverse_lazy("blog:all")






















