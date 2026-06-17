from django.views.generic import DetailView, ListView

from apps.shop.models import Product

class ProductListView(ListView):
    model = Product
    template_name = "shop/product/list.html"
    context_object_name = "products"
    
    def get_queryset(self):
       return Product.objects.active()

class ProductDetailView(DetailView):
    model = Product
    template_name = "shop/product/detail.html"
    context_object_name = "product"
    slug_field = 'slug'
    slug_url_kwargs = 'slug'
