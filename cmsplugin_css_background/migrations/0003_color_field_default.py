# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_css_background', '0002_filercssbackground'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cssbackground',
            name='attachment',
            field=models.CharField(max_length=8, default='scroll', choices=[('fixed', 'Fixed'), ('scroll', 'Scrolling')]),
        ),
        migrations.AlterField(
            model_name='cssbackground',
            name='bg_position',
            field=models.CharField(max_length=24, default='0% 0%', blank=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='cssbackground',
            name='color',
            field=models.CharField(max_length=32, blank=True, default='transparent'),
        ),
        migrations.AlterField(
            model_name='cssbackground',
            name='repeat',
            field=models.CharField(max_length=16, default='repeat', verbose_name='Tiling', choices=[('repeat', 'Tile in both directions'), ('repeat-x', 'Tile horizontally'), ('repeat-y', 'Tile vertically'), ('no-repeat', 'No tiling')]),
        ),
    ]
    if apps.is_installed('filer'):
        operations += [
            migrations.AlterField(
                model_name='filercssbackground',
                name='attachment',
                field=models.CharField(max_length=8, default='scroll', choices=[('fixed', 'Fixed'), ('scroll', 'Scrolling')]),
            ),
            migrations.AlterField(
                model_name='filercssbackground',
                name='bg_position',
                field=models.CharField(max_length=24, default='0% 0%', blank=True, verbose_name='Position'),
            ),
            migrations.AlterField(
                model_name='filercssbackground',
                name='color',
                field=models.CharField(max_length=32, blank=True, default='transparent'),
            ),
            migrations.AlterField(
                model_name='filercssbackground',
                name='repeat',
                field=models.CharField(max_length=16, default='repeat', verbose_name='Tiling', choices=[('repeat', 'Tile in both directions'), ('repeat-x', 'Tile horizontally'), ('repeat-y', 'Tile vertically'), ('no-repeat', 'No tiling')]),
            ),
        ]
