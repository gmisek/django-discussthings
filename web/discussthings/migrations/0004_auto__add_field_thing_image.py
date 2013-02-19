# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Thing.image'
        db.add_column('discussthings_thing', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Thing.image'
        db.delete_column('discussthings_thing', 'image')


    models = {
        'discussthings.response': {
            'Meta': {'object_name': 'Response'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discussthings.Response']", 'null': 'True'}),
            'topic_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discussthings.Topic']"})
        },
        'discussthings.thing': {
            'Meta': {'object_name': 'Thing'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'discussthings.topic': {
            'Meta': {'object_name': 'Topic'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thing_id': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['discussthings.Thing']"})
        }
    }

    complete_apps = ['discussthings']