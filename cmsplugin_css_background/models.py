
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _

try:
    from cms.models.pluginmodel import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        return instance.get_media_path(filename)


class CssBackground(CMSPlugin):
    '''
    A CSS background definition.
    '''
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

    color = models.CharField(max_length=32, blank=True, default=u'transparent')
    image = models.ImageField(upload_to=get_plugin_media_path)
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
        default=u'0% 0%'
    )
    # TODO: implement fields for -clip, -origin and -size css properties
    forced = models.BooleanField(
        default=False,
        help_text=_(u'Mark CSS rules as important.')
    )

    @property
    def bg_image(self):
        return u'url({})'.format(self.image.url) if self.image else u''

    def as_single_rule(self):
        bits = []
        for prop in ('color', 'image', 'repeat', 'attachment', 'position'):
            v = getattr(self, self.__CSS_FIELDNAME_MAP__.get(prop, prop))
            if v:
                bits.append(v)
        if self.forced:
            bits.append(u'!important')

        return u'background: {};'.format(' '.join(filter(None, bits)))

    def as_separate_rules(self):
        rules = {}
        for prop in ('color', 'image', 'repeat', 'attachment', 'position'):
            fieldname = self.__CSS_FIELDNAME_MAP__.get(prop) or prop
            value = getattr(self, fieldname)
            if value:
                rules[prop] = value
        important = u' !important' if self.forced else u''
        return u'\n'.join((
            u'background-{}: {}{};'.format(k, v, important)
            for k, v in rules.items()
        ))
