from django.shortcuts import render
from django.views.generic import DetailView, ListView
from apps.blog.models import Post, PostCategory

class PostListView(ListView):
    model = Post
    template_name = "blog/post/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.published()

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post/detail.html"
    context_object_name = "post"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'    

class PostCategoryDetailView(DetailView):
    model = PostCategory
    template_name = "blog/category/detail.html"
    context_object_name = "category"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.published()
        return context
