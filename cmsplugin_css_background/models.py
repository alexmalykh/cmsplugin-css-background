
import six
from cms.models.pluginmodel import CMSPlugin
from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
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

    div_id =  models.CharField(max_length=32, blank=True, default='',
        help_text=_("Unique id for the added div element"))
    div_classes =  models.CharField(max_length=64, blank=True, default='',
        help_text=_("Classes for the added div element"))

    color = models.CharField(max_length=32, blank=True, default='')
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
        default='0% 0%'
    )
    # TODO: implement fields for -clip, -origin and -size css properties
    forced = models.BooleanField(
        default=False,
        help_text=_('Mark CSS rules as important.')
    )

    def clean(self):
        errors = []
        if not self.image and not self.color and not self.div_id and not self.div_classes:
            errors.append(ValidationError(_('Must specify at least one of: color, image, id or class.'), code='empty'))
        params = {'ids': [o.div_id for o in self._meta.model.objects.filter(placeholder=self.placeholder) if o.div_id]}
        if self.div_id and self.div_id in params['ids']:
            errors.append(ValidationError(_('Div id must be unique within a page. Used values: %(ids)s'),
                code='repeated_id', params=params))
        if errors:
            raise ValidationError(errors)

    @property
    def bg_image(self):
        if self.image:
            rv = six.text_type('url({})').format(self.image.url)
        else:
            rv = six.text_type('')
        return rv

    def as_single_rule(self):
        # NOTE: When using the shorthand background property, blank properties will
        # inherit their individual property default and override less-specific CSS
        bits = []
        for prop in ('color', 'image', 'repeat', 'attachment', 'position'):
            v = getattr(self, self.__CSS_FIELDNAME_MAP__.get(prop, prop))
            if v:
                bits.append(v)
        if self.forced:
            bits.append(six.text_type('!important'))

        return six.text_type('background: {};').format(' '.join(filter(None, bits)))

    def as_separate_rules(self):
        rules = {}
        for prop in ('color', 'image', 'repeat', 'attachment', 'position'):
            fieldname = self.__CSS_FIELDNAME_MAP__.get(prop) or prop
            value = getattr(self, fieldname)
            if value:
                rules[prop] = value
        important = u' !important' if self.forced else u''
        return '\n'.join([
            six.text_type('background-{}: {}{};').format(k, v, important)
            for k, v in rules.items()
        ])

    def __six_repr(self):
        items = []
        if self.div_id:
            items.append('id="{}"'.format(self.div_id))
        if self.div_classes:
            items.append('class="{}"'.format(self.div_classes))
        if self.color:
            items.append(self.color)
        if self.image:
            items.append(self.image.url)

        if items:
            rv = ' '.join(items)
        else:
            rv = '{} [-----]'.format(self.pk)
        return six.text_type(rv)

    if six.PY3:
        __str__ = __six_repr
    elif six.PY2:
        __unicode__ = __six_repr


class CssBackground(CssBackgroundAbstractBase):
    '''
    A CSS Background definition plugin.
    '''
    image = models.ImageField(upload_to=get_plugin_media_path, null=True, blank=True)


try:
    from filer.fields.image import FilerImageField
except ImportError:
    pass
else:
    if 'filer' in settings.INSTALLED_APPS:
        class FilerCssBackground(CssBackgroundAbstractBase):
            '''
            A CSS Background definition plugin, adapted for django-filer.
            '''
            image = FilerImageField(null=True, blank=True)
