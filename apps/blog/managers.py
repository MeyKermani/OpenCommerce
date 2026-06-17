from django.db import models
from apps.blog.choices import PostStatus
class PostManager(models.Manager):
    def published(self):
        return self.get_queryset().filter(status=PostStatus.PUBLISHED )
   