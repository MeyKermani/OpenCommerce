from django.contrib import admin
from django.urls import path
from apps.blog.views import PostDetailView, PostListView
app_name = "apps.blog"

urlpatterns = [
    path("", PostListView.as_view() ,"post_list"),
    path("post/<slug:slug>", PostDetailView.as_view() , "post_detail"),

]
