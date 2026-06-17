from django.db import models
from helpers.models.timestamp import TimeStampedModel
from apps.common.models import Tag
from apps.shop.choices import ProductStatus
from apps.shop.managers import ProductManager


class ProductCategory(TimeStampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    

class Product(TimeStampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products'
    )
    description = models.TextField()
    tags = models.ManyToManyField(
        Tag,
        related_name="products",
        blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(
        max_length=50,
        choices=ProductStatus.choices,
        default= ProductStatus.ACTIVE 
    )
    objects = ProductManager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_at"]