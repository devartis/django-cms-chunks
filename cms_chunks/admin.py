#! coding: utf-8
from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import Chunk

admin.site.register(Chunk, PlaceholderAdmin)

__author__ = 'lgomez'
