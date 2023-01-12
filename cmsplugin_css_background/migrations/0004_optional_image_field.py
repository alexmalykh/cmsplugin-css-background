# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.db import migrations, models
import cms.models.pluginmodel

try:
    import filer.fields.image
except ImportError:
    FILER = False
else:
    FILER = apps.is_installed('filer')


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_css_background', '0003_color_field_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cssbackground',
            name='image',
            field=models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, help_text='Leave blank to fall back to previously applied CSS rule.', null=True, blank=True),
        ),
    ]
    if FILER:
        dependencies.insert(0, ('filer', '__first__'))
        operations += [
            migrations.AlterField(
                model_name='filercssbackground',
                name='image',
                field=filer.fields.image.FilerImageField(help_text='Leave blank to fall back to previously applied CSS rule.', null=True, blank=True, to='filer.Image', on_delete=models.SET_NULL),
            ),
        ]
