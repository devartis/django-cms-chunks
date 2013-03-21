from django.db import models
from cms.models.fields import PlaceholderField
from managers import ChunkManager


class Chunk(models.Model):
    tags = models.CharField(max_length=200)
    code = PlaceholderField('chunk_placeholder', related_name="chunks")
    priority = models.IntegerField()

    objects = ChunkManager()

    def __unicode__(self):
        return "Tags: %s. Priority: %s" % (self.tags, self.priority)

    def has_tag(self, tag):
        tags = [string.strip() for string in str(self.tags).split(",")]
        return tag in tags

# Create your models here.
