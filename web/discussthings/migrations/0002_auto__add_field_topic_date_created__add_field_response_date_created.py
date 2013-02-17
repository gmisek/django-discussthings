# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Topic.date_created'
        db.add_column('discussthings_topic', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Response.date_created'
        db.add_column('discussthings_response', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Topic.date_created'
        db.delete_column('discussthings_topic', 'date_created')

        # Deleting field 'Response.date_created'
        db.delete_column('discussthings_response', 'date_created')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'discussthings.topic': {
            'Meta': {'object_name': 'Topic'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['discussthings']