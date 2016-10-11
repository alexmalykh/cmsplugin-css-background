
from __future__ import absolute_import, unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import CssBackground


class CssBackgroundPlugin(CMSPluginBase):
    model = CssBackground
    fields = ('color', 'image',
              'repeat', 'attachment', 'bg_position',
              'forced')
    name = _('CSS Background image')
    render_template = 'cmsplugin_css_background/css-background.html'
    allow_children = False

plugin_pool.register_plugin(CssBackgroundPlugin)


try:
    from .models import FilerCssBackground
except ImportError:
    pass
else:
    class FilerCssBackgroundPlugin(CssBackgroundPlugin):
        model = FilerCssBackground
        module = 'Filer'
    plugin_pool.register_plugin(FilerCssBackgroundPlugin)
