
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_cascade.mixins import TransparentMixin

from .models import CssBackground


class CssBackgroundPlugin(TransparentMixin, CMSPluginBase):
    model = CssBackground
    fields = ('color', 'image',
              'repeat', 'attachment', 'bg_position',
              'div_id', 'div_classes',
              'forced')
    name = _('CSS Background')
    render_template = 'cms/plugins/css-bgwrapper.html'
    require_parent = False
    parent_classes = None
    allow_children = True
    child_classes = None

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
