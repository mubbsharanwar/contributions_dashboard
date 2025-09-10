from django.db import models
from django.utils.text import slugify
from cms.models.pluginmodel import CMSPlugin


class Document(models.Model):
    """
    Parent model to hold all documents (like DocumentsIndexPage in Wagtail).
    """
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class DocumentLink(models.Model):
    """
    Store links for a document (replaces Wagtail’s StreamField with StructBlock).
    """
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        related_name="links"
    )
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f"{self.title} ({self.url})"


class DocumentPluginModel(CMSPlugin):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title