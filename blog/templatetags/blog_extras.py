from django.contrib.auth.models import User
from django import template
from django.utils.html import format_html
register = template.Library()


@register.simple_tag(takes_context=True)
def author_details(context):
  request = context["request"]
  current_user = request.user
  post = context["post"]
  author = post.author

  if author == current_user:
    return format_html("<strong>me</strong>")

  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"

  return format_html("{}", name)

@register.simple_tag
def row(extra_classes=""):
    return format_html('<div class="row">', extra_classes)

@register.simple_tag
def endrow():
    return format_html('</div>')

@register.simple_tag
def col(extra_classes=""):
    return format_html('<div class="col">', extra_classes)

@register.simple_tag
def endcol(extra_classes=""):
    return format_html('</div>', extra_classes)

