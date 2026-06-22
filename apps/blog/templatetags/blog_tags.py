from django import template
from apps.blog.models import Post, PostCategory

register = template.Library()


@register.inclusion_tag('blog/partials/_latest_posts.html')
def latest_posts(count=5):
    posts = Post.objects.all()[:count]
    return {'latest_posts':posts}

@register.inclusion_tag('blog/partials/_post_catgeories.html')
def post_catgeories():
    categories = PostCategory.objects.all()
    return {'post_catgeories':categories}

