from django.contrib import admin
from apps.blog.models import PostCategory, Post


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','created_at', 'updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','created_at', 'updated_at')
    search_fields = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)
