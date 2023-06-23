from django import template
from MyMusicApp.albums.models import models

register = template.Library()


@register.filter(name="price_filter")
def price_filter(price):
    return "%.2f" % price
