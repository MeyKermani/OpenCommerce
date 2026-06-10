from django.contrib import admin
from django.urls import path

app_name = "apps.blog"

urlpatterns = [
    path("", "post_list"),
    path("post/<slug:slug>", "post_detail"),

]
