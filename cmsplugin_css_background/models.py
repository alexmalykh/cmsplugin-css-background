
from __future__ import unicode_literals

import sys

from cms.models.pluginmodel import CMSPlugin
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import force_text
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
        ('',            _('Not specified')),
        ('repeat',      _('Tile in both directions')),
        ('repeat-x',    _('Tile horizontally')),
        ('repeat-y',    _('Tile vertically')),
        ('no-repeat',   _('No tiling')),
    )

    ATTACHMENT_CHOICES = (
        ('',        _('Not specified')),
        ('fixed',   _('Fixed')),
        ('scroll',  _('Scrolling')),
    )

    __CSS_FIELDNAME_MAP__ = {
        'image':    'bg_image',
        'position': 'bg_position'
    }

    _blank_help = _('Leave blank to fall back to previously applied CSS rule.')

    color = models.CharField(
        max_length=32,
        blank=True,
        default='',
        help_text=_blank_help
    )
    repeat = models.CharField(
        _('Tiling'),
        max_length=16,
        choices=REPEAT_CHOICES,
        blank=True,
        default=''
    )
    attachment = models.CharField(
        max_length=8,
        choices=ATTACHMENT_CHOICES,
        blank=True,
        default=''
    )
    bg_position = models.CharField(
        _('Position'),
        max_length=24,
        blank=True,
        default='',
        help_text=_blank_help
    )
    # TODO: implement fields for -clip, -origin and -size css properties
    forced = models.BooleanField(
        default=False,
        help_text=_('Mark CSS rules as important.')
    )

    def clean(self):
        if not (self.color or self.image):
            raise ValidationError(_('Color or image must be provided at least.'))

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
        # NOTE: When using the shorthand background property, blank properties will
        # have their individual property default and won't cascade down
        # to corresponding lower-priority rules.
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
        # or '/path/to/image.jpg over #aabbcc'
        # or 'no image/color'
        bits = [self.get_image_url(), self.color]
        s = _(' over ').join(filter(None, bits)) or _('no image/color')
        return force_text(s)

    if sys.version_info.major > 2:
        __str__ = __string_repr
    else:
        __unicode__ = __string_repr


class CssBackground(CssBackgroundAbstractBase):
    '''
    A CSS Background definition plugin.
    '''
    image = models.ImageField(
        upload_to=get_plugin_media_path,
        null=True,
        blank=True,
        help_text=CssBackgroundAbstractBase._blank_help
    )

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
            image = FilerImageField(
                on_delete=models.SET_NULL,
                null=True,
                blank=True,
                help_text=CssBackgroundAbstractBase._blank_help
            )

            def get_image_url(self):
                return self.image.url if self.image_id else ''
