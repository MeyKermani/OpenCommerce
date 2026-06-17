from django.db import models
from apps.shop.choices import ProductStatus
class ProductManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(status=ProductStatus.ACTIVE )
   