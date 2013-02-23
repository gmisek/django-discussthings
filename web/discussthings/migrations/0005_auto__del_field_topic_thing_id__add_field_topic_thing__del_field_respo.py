# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Topic.thing_id'
        db.delete_column('discussthings_topic', 'thing_id_id')

        # Adding field 'Topic.thing'
        db.add_column('discussthings_topic', 'thing',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['discussthings.Thing']),
                      keep_default=False)

        # Deleting field 'Response.parent_id'
        db.delete_column('discussthings_response', 'parent_id_id')

        # Deleting field 'Response.topic_id'
        db.delete_column('discussthings_response', 'topic_id_id')

        # Adding field 'Response.topic'
        db.add_column('discussthings_response', 'topic',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['discussthings.Topic']),
                      keep_default=False)

        # Adding field 'Response.parent'
        db.add_column('discussthings_response', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['discussthings.Response']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Topic.thing_id'
        db.add_column('discussthings_topic', 'thing_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['discussthings.Thing']),
                      keep_default=False)

        # Deleting field 'Topic.thing'
        db.delete_column('discussthings_topic', 'thing_id')

        # Adding field 'Response.parent_id'
        db.add_column('discussthings_response', 'parent_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discussthings.Response'], null=True),
                      keep_default=False)

        # Adding field 'Response.topic_id'
        db.add_column('discussthings_response', 'topic_id',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['discussthings.Topic']),
                      keep_default=False)

        # Deleting field 'Response.topic'
        db.delete_column('discussthings_response', 'topic_id')

        # Deleting field 'Response.parent'
        db.delete_column('discussthings_response', 'parent_id')


    models = {
        'discussthings.response': {
            'Meta': {'object_name': 'Response'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discussthings.Response']"}),
            'topic': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['discussthings.Topic']"})
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
            'thing': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['discussthings.Thing']"})
        }
    }

    complete_apps = ['discussthings']