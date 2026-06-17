from django.contrib import admin
from django.urls import path
from apps.shop.views import ProductDetailView, ProductListView, ProductCategoryDetailView
app_name = "apps.shop"

urlpatterns = [
    path("", ProductListView.as_view() ,name="product_list"),
    path("product/<slug:slug>", ProductDetailView.as_view() , name="product_detail"),
    path('categories/<slug:slug>', ProductCategoryDetailView.as_view(), name="category_detail" )

]
