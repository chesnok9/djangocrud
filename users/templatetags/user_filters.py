from django import template
from dateutil.relativedelta import relativedelta
from datetime import *

register = template.Library()

@register.filter(name='allowed')
def allowed(date):
    today = datetime.now()
    years = relativedelta(today, date).years
    return 'allowed' if years > 13 else 'blocked'

@register.filter(name='bizzfuzz')
def bizzfuzz(value):
    res = ''
    if (value % 3 == 0) and (value % 5 == 0):
        res = 'BizzFuzz'
    elif value % 3 == 0:
        res = 'Bizz'
    elif value % 5 == 0:
        res = 'Fuzz'


    return res