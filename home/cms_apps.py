from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _

class DocumentPagesApphook(CMSApp):
    app_name = "home"
    name = _("Document Pages")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["home.urls"]

apphook_pool.register(DocumentPagesApphook)
