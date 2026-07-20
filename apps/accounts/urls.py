from django.contrib import admin
from django.urls import path
from apps.accounts.views import CustomLoginView, CustomLogoutView, SignupView, ProfileView, ProfileUpdateView
app_name = "apps.accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view() ,name="login"),
    path("logout/", CustomLogoutView.as_view() ,name="logout"),
    path("signup/", SignupView.as_view() ,name="signup"),
    path("profile/", ProfileView.as_view(), name="profile" ),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile_edit" )


]
