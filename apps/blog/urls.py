from django.contrib import admin
from django.urls import path
from apps.blog.views import PostDetailView, PostListView, PostCategoryDetailView
app_name = "apps.blog"

urlpatterns = [
    path("", PostListView.as_view() ,name="post_list"),
    path("post/<slug:slug>", PostDetailView.as_view() , name="post_detail"),
    path('categories/<slug:slug>', PostCategoryDetailView.as_view(), name="category_detail")
]
