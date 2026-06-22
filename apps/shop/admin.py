from django.contrib import admin
from apps.shop.models import ProductCategory, Product
from apps.shop.utils import format_price_toman

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','created_at', 'updated_at')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'display_price', 'stock','created_at', 'updated_at')
    search_fields = ('title','price')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)

    @admin.display(description="Price")
    def display_price(self, product):
        return format_price_toman(product.price)