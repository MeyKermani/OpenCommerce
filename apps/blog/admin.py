from django.contrib import admin
from apps.blog.models import PostCategory, Post

admin.site.register(PostCategory)
admin.site.register(Post)
