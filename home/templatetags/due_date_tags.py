from django import template
from django.template.defaultfilters import stringfilter
from tasks.models import DueDateChoice, Status

register = template.Library()

@register.filter
@stringfilter
def due_date_display(value):
    return DueDateChoice(int(value)).name.replace('_', ' ')

@register.filter
@stringfilter
def status_display(value):
    return Status(int(value)).name.replace('_', ' ')