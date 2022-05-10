# -*- coding: utf-8 -*-
#
# http://djangosnippets.org/snippets/1550/
#
# https://opensourcehacker.com/2013/05/16/putting-breakpoints-to-html-templates-in-python/
#
# To do debugging in template
# I: {% load debug %}
# II: place this {% pdb %} wherever you want to debug in the code


import pdb as pdb_module

from django.template import Library, Node

register = Library()


class PdbNode(Node):
    def render(self, context):
        pdb_module.set_trace()
        return ''


@register.tag
def pdb(parser, token):
    return PdbNode()
