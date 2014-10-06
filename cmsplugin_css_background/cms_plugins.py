
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import CssBackground


class CssBackgroundPlugin(CMSPluginBase):
    model = CssBackground
    name = _('Background CSS definition')
    render_template = 'cms/plugins/css-background.html'
    allow_children = False

plugin_pool.register_plugin(CssBackgroundPlugin)
