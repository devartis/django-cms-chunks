# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Chunk'
        db.create_table('cms_chunks_chunk', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('code', self.gf('django.db.models.fields.related.ForeignKey')(related_name='chunks', null=True, to=orm['cms.Placeholder'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cms_chunks', ['Chunk'])


    def backwards(self, orm):
        # Deleting model 'Chunk'
        db.delete_table('cms_chunks_chunk')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cms_chunks.chunk': {
            'Meta': {'object_name': 'Chunk'},
            'code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'chunks'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['cms_chunks']