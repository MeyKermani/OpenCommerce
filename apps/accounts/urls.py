from django.contrib import admin
from django.urls import path
from apps.accounts.views import CustomLoginView, CustomLogoutView
app_name = "apps.accounts"

urlpatterns = [
    path("login/", CustomLoginView.as_view() ,name="login"),
    path("logout/", CustomLogoutView.as_view() ,name="logout")

]
