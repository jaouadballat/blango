from django.contrib.auth.models import User
from django import template

register = template.Library()


@register.filter(name="author_details")
def author_details(author):
  if not isinstance(author, User):
    return ''
  if author.first_name and author.last_name:
    return f"{author.first_name}"
  else:
    return f"{author.username}"
