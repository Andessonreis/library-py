from django import template


register = template.Library()

@register.filter   #declarando que issoé um filtro do django
def shows_duration_time(value1, value2):
    if value1 is not None and value2 is not None:
        return (value1 - value2).days
    return ''