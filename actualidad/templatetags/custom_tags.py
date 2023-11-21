from django import template

register = template.Library()

@register.filter
def split_two_rows(value):
    count = len(value.split())
    divide = int(count) / 2
    first = value.split()[:int(divide)]
    last = value.split()[int(divide):]
    complete = ' '.join(map(str, first))
    complete += ' '.join(map(str, last))
    
    try:
        return complete
    except (ValueError, ZeroDivisionError):
        return None