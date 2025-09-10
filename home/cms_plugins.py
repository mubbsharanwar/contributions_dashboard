from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from home.models import DocumentPluginModel
from django.utils.translation import gettext as _


@plugin_pool.register_plugin  # register the plugin
class DocumentPlugin(CMSPluginBase):
    model = DocumentPluginModel 
    module = _("Document")
    name = _("Document Plugin")
    render_template = "documents/document_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context