
from __future__ import unicode_literals

import sys

from cms.models.pluginmodel import CMSPlugin
from django.apps import apps as django_apps
from django.db import models
from django.utils.translation import ugettext_lazy as _

try:
    from cms.models.pluginmodel import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        return instance.get_media_path(filename)


class CssBackgroundAbstractBase(CMSPlugin):
    '''
    Abstract model base class for CssBackground and FilerCssBackground.
    '''
    class Meta:
        abstract = True

    REPEAT_CHOICES = (
        ('repeat',      _('Tile in both directions')),
        ('repeat-x',    _('Tile horizontally')),
        ('repeat-y',    _('Tile vertically')),
        ('no-repeat',   _('No tiling')),
    )

    ATTACHMENT_CHOICES = (
        ('fixed',   _('Fixed')),
        ('scroll',  _('Scrolling')),
    )

    __CSS_FIELDNAME_MAP__ = {
        'image':    'bg_image',
        'position': 'bg_position'
    }

    # NOTE: fields default values are set
    #       to conform defaults defined in W3 CSS specs

    color = models.CharField(max_length=32, blank=True, default='transparent')
    repeat = models.CharField(
        _('Tiling'),
        max_length=16,
        choices=REPEAT_CHOICES,
        default='repeat'
    )
    attachment = models.CharField(
        max_length=8,
        choices=ATTACHMENT_CHOICES,
        default='scroll'
    )
    bg_position = models.CharField(
        _('Position'),
        max_length=24,
        blank=True,
        default='0% 0%'
    )
    # TODO: implement fields for -clip, -origin and -size css properties
    forced = models.BooleanField(
        default=False,
        help_text=_('Mark CSS rules as important.')
    )

    def get_image_url(self):
        raise NotImplementedError(
            'subclasses of CssBackgroundAbstractBase '
            'must provide a get_image_url() method.'
        )

    @property
    def bg_image(self):
        url = self.get_image_url()
        return 'url({})'.format(url) if url else ''

    def as_single_rule(self):
        bits = []
        for prop in ('color', 'image', 'repeat', 'attachment', 'position'):
            v = getattr(self, self.__CSS_FIELDNAME_MAP__.get(prop, prop))
            if v:
                bits.append(v)
        if self.forced:
            bits.append('!important')

        return 'background: {};'.format(' '.join(filter(None, bits)))

    def as_separate_rules(self):
        rules = {}
        for prop in ('color', 'image', 'repeat', 'attachment', 'position'):
            fieldname = self.__CSS_FIELDNAME_MAP__.get(prop) or prop
            value = getattr(self, fieldname)
            if value:
                rules[prop] = value
        important = u' !important' if self.forced else u''
        return '\n'.join([
            'background-{}: {}{};'.format(k, v, important)
            for k, v in rules.items()
        ])

    def __string_repr(self):
        # render strings like
        # '/path/to/image.jpg' or '#aabbcc'
        # or '/path/to/image.jpg on #aabbcc'
        # or 'no image/color'
        bits = [self.get_image_url(), self.color]
        return _(' on ').join(filter(None, bits)) or _('no image/color')

    if sys.version_info.major > 2:
        __str__ = __string_repr
    else:
        __unicode__ = __string_repr


class CssBackground(CssBackgroundAbstractBase):
    '''
    A CSS Background definition plugin.
    '''
    image = models.ImageField(upload_to=get_plugin_media_path)

    def get_image_url(self):
        return self.image.url if self.image else ''

try:
    from filer.fields.image import FilerImageField
except ImportError:
    pass
else:
    if django_apps.is_installed('filer'):
        class FilerCssBackground(CssBackgroundAbstractBase):
            '''
            A CSS Background definition plugin, adapted for django-filer.
            '''
            image = FilerImageField()

            def get_image_url(self):
                return self.image.url if self.image_id else ''
