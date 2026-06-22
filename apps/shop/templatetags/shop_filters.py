from django import template
from apps.shop.utils import format_price_toman

register = template.Library()

@register.filter
def to_toman(value):
    return format_price_toman(value)