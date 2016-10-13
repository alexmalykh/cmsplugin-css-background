# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import apps
from django.db import migrations, models


FILER = apps.is_installed('filer')


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_css_background', '0004_optional_image_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cssbackground',
            name='attachment',
            field=models.CharField(blank=True, max_length=8, choices=[('', 'Inherit'), ('fixed', 'Fixed'), ('scroll', 'Scrolling')], default=''),
        ),
        migrations.AlterField(
            model_name='cssbackground',
            name='bg_position',
            field=models.CharField(verbose_name='Position', max_length=24, help_text='Leave blank to fall back to previously applied CSS rule.', default='', blank=True),
        ),
        migrations.AlterField(
            model_name='cssbackground',
            name='color',
            field=models.CharField(blank=True, max_length=32, help_text='Leave blank to fall back to previously applied CSS rule.', default='transparent'),
        ),
        migrations.AlterField(
            model_name='cssbackground',
            name='repeat',
            field=models.CharField(verbose_name='Tiling', max_length=16, choices=[('', 'Inherit'), ('repeat', 'Tile in both directions'), ('repeat-x', 'Tile horizontally'), ('repeat-y', 'Tile vertically'), ('no-repeat', 'No tiling')], default='', blank=True),
        ),
    ]

    if FILER:
        operations += [
            migrations.AlterField(
                model_name='filercssbackground',
                name='attachment',
                field=models.CharField(blank=True, max_length=8, choices=[('', 'Inherit'), ('fixed', 'Fixed'), ('scroll', 'Scrolling')], default=''),
            ),
            migrations.AlterField(
                model_name='filercssbackground',
                name='bg_position',
                field=models.CharField(verbose_name='Position', max_length=24, help_text='Leave blank to fall back to previously applied CSS rule.', default='', blank=True),
            ),
            migrations.AlterField(
                model_name='filercssbackground',
                name='color',
                field=models.CharField(blank=True, max_length=32, help_text='Leave blank to fall back to previously applied CSS rule.', default='transparent'),
            ),
            migrations.AlterField(
                model_name='filercssbackground',
                name='repeat',
                field=models.CharField(verbose_name='Tiling', max_length=16, choices=[('', 'Inherit'), ('repeat', 'Tile in both directions'), ('repeat-x', 'Tile horizontally'), ('repeat-y', 'Tile vertically'), ('no-repeat', 'No tiling')], default='', blank=True),
            ),
        ]
