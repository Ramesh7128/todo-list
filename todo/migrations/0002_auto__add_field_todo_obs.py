# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Todo.obs'
        db.add_column(u'todo_todo', 'obs',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Todo.obs'
        db.delete_column(u'todo_todo', 'obs')


    models = {
        u'todo.todo': {
            'Meta': {'object_name': 'Todo'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'todos'", 'to': u"orm['todo.TodoCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'obs': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'todo.todocategory': {
            'Meta': {'object_name': 'TodoCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['todo']