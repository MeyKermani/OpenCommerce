from django.db import models
from helpers.models.timestamp import TimeStampedModel

class ProductCategory(TimeStampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title