from django import template

register = template.Library()


@register.filter
def to_str(value):
    """converts to string"""
    return str(value)


@register.filter
def to_plus(value):
    """converts to + url formate"""
    return str(value).replace(" ", "-")


@register.filter
def to_title(value):
    """converts to + url formate"""
    return str(value).title()
