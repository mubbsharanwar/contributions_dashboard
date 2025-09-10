from django.shortcuts import render, get_object_or_404
from .models import Document, DocumentLink

def document_index(request):
    documents = Document.objects.all()
    return render(request, "documents/index.html", {"documents": documents})

def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    links = DocumentLink.objects.filter(document=document)
    return render(request, "documents/detail.html", {"document": document, "links": links})
