from django.contrib import admin
from apps.common.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)
    
