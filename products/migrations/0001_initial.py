# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Media'
        db.create_table(u'products_media', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'products', ['Media'])

        # Adding model 'Category'
        db.create_table(u'products_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'products', ['Category'])

        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sold_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'products', ['Product'])

        # Adding M2M table for field photos on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('media', models.ForeignKey(orm[u'products.media'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'media_id'])

        # Adding M2M table for field category on 'Product'
        m2m_table_name = db.shorten_name(u'products_product_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'products.product'], null=False)),
            ('category', models.ForeignKey(orm[u'products.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Media'
        db.delete_table(u'products_media')

        # Deleting model 'Category'
        db.delete_table(u'products_category')

        # Deleting model 'Product'
        db.delete_table(u'products_product')

        # Removing M2M table for field photos on 'Product'
        db.delete_table(db.shorten_name(u'products_product_photos'))

        # Removing M2M table for field category on 'Product'
        db.delete_table(db.shorten_name(u'products_product_category'))


    models = {
        u'products.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'products.media': {
            'Meta': {'object_name': 'Media'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['products.Media']", 'symmetrical': 'False'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sold_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['products']