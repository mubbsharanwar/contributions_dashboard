from django.contrib import admin
from .models import Document, DocumentLink


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ["title"]


@admin.register(DocumentLink)
class DocumentLinkAdmin(admin.ModelAdmin):
    list_display = ("title", "url")
    search_fields = ["title"]
