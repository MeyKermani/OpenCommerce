from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import UserProfile
from django.contrib.auth import get_user_model


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_diplay = ('user','mobile_number')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'mobile_number')