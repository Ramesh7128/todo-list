# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TodoCategory'
        db.create_table(u'todo_todocategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'todo', ['TodoCategory'])

        # Adding model 'Todo'
        db.create_table(u'todo_todo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='todos', to=orm['todo.TodoCategory'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'todo', ['Todo'])


    def backwards(self, orm):
        # Deleting model 'TodoCategory'
        db.delete_table(u'todo_todocategory')

        # Deleting model 'Todo'
        db.delete_table(u'todo_todo')


    models = {
        u'todo.todo': {
            'Meta': {'object_name': 'Todo'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'todos'", 'to': u"orm['todo.TodoCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'todo.todocategory': {
            'Meta': {'object_name': 'TodoCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['todo']