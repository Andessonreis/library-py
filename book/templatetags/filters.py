from django import template
from datetime import date, datetime


register = template.Library()

@register.filter
def shows_duration_time(value1, value2):
    if isinstance(value1, datetime) and isinstance(value2, datetime):
        difference = value1 - value2
        return f"{difference.days} Days" if difference.days >= 0 else 'Ainda não devolvido!'
    return 'Ainda não devolvido!'
