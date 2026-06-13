from django.contrib import admin
from django.urls import path
from apps.shop.views import ProductDetailView, ProductListView
app_name = "apps.shop"

urlpatterns = [
    path("", ProductListView.as_view() ,name="product_list"),
    path("product/<slug:slug>", ProductDetailView.as_view() , name="product_detail"),

]
