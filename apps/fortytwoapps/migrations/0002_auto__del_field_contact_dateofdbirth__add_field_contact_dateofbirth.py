# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Contact.dateofdbirth'
        db.delete_column(u'fortytwoapps_contact', 'dateofdbirth')

        # Adding field 'Contact.dateofbirth'
        db.add_column(u'fortytwoapps_contact', 'dateofbirth',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2018, 9, 3, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Contact.dateofdbirth'
        db.add_column(u'fortytwoapps_contact', 'dateofdbirth',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2018, 9, 3, 0, 0)),
                      keep_default=False)

        # Deleting field 'Contact.dateofbirth'
        db.delete_column(u'fortytwoapps_contact', 'dateofbirth')


    models = {
        u'fortytwoapps.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'dateofbirth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'othercontacts': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['fortytwoapps']