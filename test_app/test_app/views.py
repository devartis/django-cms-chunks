#! coding: utf-8
from django.views.generic import TemplateView


class Chunks(TemplateView):
    template_name = "test_template.html"


__author__ = 'lgomez'
