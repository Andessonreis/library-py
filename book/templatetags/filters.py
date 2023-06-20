from django import template


register = template.Library()

@register.filter   #declarando que issoé um filtro do django
def shows_duration_time(value1, value2):
    return (value1 - value2).days
