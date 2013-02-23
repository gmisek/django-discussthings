# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Response.parent'
        db.alter_column('discussthings_response', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discussthings.Response'], null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Response.parent'
        raise RuntimeError("Cannot reverse this migration. 'Response.parent' and its values cannot be restored.")

    models = {
        'discussthings.response': {
            'Meta': {'object_name': 'Response'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discussthings.Response']", 'null': 'True'}),
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