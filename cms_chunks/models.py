from django.db import models
from cms.models.fields import PlaceholderField


class Chunk(models.Model):
    tags = models.CharField(max_length=200)
    code = PlaceholderField('chunk_placeholder', related_name="chunks")
    priority = models.IntegerField()

# Create your models here.
