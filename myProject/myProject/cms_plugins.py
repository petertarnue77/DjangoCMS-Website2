from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from .models import NewsPlogin


@plugin_pool.register_plugin
class About_JACI_Plugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "index.html"
    cache = False


@plugin_pool.register_plugin
class News_Plugin(CMSPluginBase):
    model = NewsPlogin
    render_template = "about_plugin.html"
    cache = False
