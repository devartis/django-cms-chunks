#! coding: utf-8

from django.db.models import Manager


class ChunkManager(Manager):
    def with_tag(self, tag_key):
        return  (chunk for chunk in self.all() if chunk.has_tag(tag_key))

__author__ = 'lgomez'
