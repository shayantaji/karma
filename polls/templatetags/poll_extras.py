from django import template
from urllib.parse import urlencode

register = template.Library()

@register.simple_tag(takes_context=True)
def query_replace(context, **kwargs):
    request = context['request']
    query = request.GET.copy()
    query.pop('page',None)

    for key,value in kwargs.items():
        if value:
            query[key] = value
        else:
            query.pop(key,None)

    query_string = query.urlencode()
    return f'?{query_string}' if query_string else ''




@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return f"{value:,}   تومان"