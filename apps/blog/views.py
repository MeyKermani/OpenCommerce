from django.shortcuts import render
from django.views.generic import DetailView, ListView
from apps.blog.models import Post

class PostListView(ListView):
    model = Post
    template_name = ""
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = ""
    context_object_name = "post"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'    

