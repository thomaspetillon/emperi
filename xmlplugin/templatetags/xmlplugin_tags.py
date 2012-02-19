# -*- coding: iso-8859-15 -*-
from django import template
from django.template.defaultfilters import stringfilter
from datetime import datetime
import re
register = template.Library()

@register.filter(name="datestr_format")
@stringfilter
def datestr_format(datestr, formats):
    """
    Convert string date using formats: "informat||outformat"
    """
    informat, outformat = formats.split('||')
    dateobj = datetime.strptime(datestr, informat)    
    return datetime.strftime(dateobj,outformat)
    
@register.filter(name="timestr_format")
@stringfilter
def timestr_format(timestr, formats):
    """
    Convert string time using formats: "informat||outformat"
    """
    informat, outformat = formats.split('||')
    timeobj = datetime.strptime(timestr, informat)    
    return datetime.strftime(timeobj,outformat)
    
    
@register.filter(name="inital_letter")
@stringfilter
def inital_letter(first_name):
    """
    output inital letter with a dot from a string
    ex : John Fitzgerald -> J. F. 
    """
    names = first_name.split(' ')
    initials =""
    for name in names:
        if name:
            initials += name[0]+'.&nbsp;'
    return initials

@register.filter(name="striphtmlcomments")
@stringfilter
def striphtmlcomments(string):
    """
    Remove html conditionnal comments ( <!--[if ...]--><!--[endif]-->) from a string
    """
    p = re.compile(r'<!--\[if[^<>]*?>.*?\[endif\]-->')
    string = p.sub('', string)  
    return string