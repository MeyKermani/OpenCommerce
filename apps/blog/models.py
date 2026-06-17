from django.db import models
from helpers.models.timestamp import TimeStampedModel
from apps.common.models import Tag
from apps.blog.choices import PostStatus
from apps.blog.managers import PostManager


class PostCategory(TimeStampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title
         


class Post(TimeStampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    body = models.TextField()
    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=PostStatus.choices,
        default=PostStatus.PUBLISHED
    )
    objects = PostManager()
    def __str__(self):
        return self.title