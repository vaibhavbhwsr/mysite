from django.template import Library
from commons.storage_backends import get_presigned_url

register = Library()


@register.filter
def pre_signed(value):
    url = get_presigned_url(value)
    return url
