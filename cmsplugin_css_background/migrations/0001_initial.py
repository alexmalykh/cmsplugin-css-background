# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CssBackground'
        db.create_table(u'cmsplugin_css_background_cssbackground', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default=u'transparent', max_length=32, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('repeat', self.gf('django.db.models.fields.CharField')(default='repeat', max_length=16)),
            ('attachment', self.gf('django.db.models.fields.CharField')(default='scroll', max_length=8)),
            ('bg_position', self.gf('django.db.models.fields.CharField')(default=u'0% 0%', max_length=24, blank=True)),
            ('forced', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cmsplugin_css_background', ['CssBackground'])


    def backwards(self, orm):
        # Deleting model 'CssBackground'
        db.delete_table(u'cmsplugin_css_background_cssbackground')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_css_background.cssbackground': {
            'Meta': {'object_name': 'CssBackground', '_ormbases': ['cms.CMSPlugin']},
            'attachment': ('django.db.models.fields.CharField', [], {'default': "'scroll'", 'max_length': '8'}),
            'bg_position': ('django.db.models.fields.CharField', [], {'default': "u'0% 0%'", 'max_length': '24', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "u'transparent'", 'max_length': '32', 'blank': 'True'}),
            'forced': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'repeat': ('django.db.models.fields.CharField', [], {'default': "'repeat'", 'max_length': '16'})
        }
    }

    complete_apps = ['cmsplugin_css_background']