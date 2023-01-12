# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CssBackground',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, on_delete=models.deletion.CASCADE, primary_key=True, related_name='cmsplugin_css_background_cssbackground', serialize=False, to='cms.CMSPlugin')),
                ('color', models.CharField(default=b'', max_length=32, blank=True)),
                ('repeat', models.CharField(default=b'repeat', max_length=16, verbose_name='Tiling', choices=[(b'repeat', 'Tile in both directions'), (b'repeat-x', 'Tile horizontally'), (b'repeat-y', 'Tile vertically'), (b'no-repeat', 'No tiling')])),
                ('attachment', models.CharField(default=b'scroll', max_length=8, choices=[(b'fixed', 'Fixed'), (b'scroll', 'Scrolling')])),
                ('bg_position', models.CharField(default=b'0% 0%', max_length=24, verbose_name='Position', blank=True)),
                ('forced', models.BooleanField(default=False, help_text='Mark CSS rules as important.')),
                ('image', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
