# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Thing'
        db.create_table('discussthings_thing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('discussthings', ['Thing'])

        # Adding model 'Topic'
        db.create_table('discussthings_topic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('discussthings', ['Topic'])

        # Adding model 'Response'
        db.create_table('discussthings_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('topic_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discussthings.Topic'])),
            ('parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['discussthings.Response'], null=True)),
        ))
        db.send_create_signal('discussthings', ['Response'])


    def backwards(self, orm):
        # Deleting model 'Thing'
        db.delete_table('discussthings_thing')

        # Deleting model 'Topic'
        db.delete_table('discussthings_topic')

        # Deleting model 'Response'
        db.delete_table('discussthings_response')


    models = {
        'discussthings.response': {
            'Meta': {'object_name': 'Response'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['discussthings']