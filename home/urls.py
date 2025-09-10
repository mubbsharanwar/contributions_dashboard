from django.urls import path
from . import views

urlpatterns = [
    path("", views.document_index, name="document_index"),
    path("<int:pk>/", views.document_detail, name="document_detail"),
]

