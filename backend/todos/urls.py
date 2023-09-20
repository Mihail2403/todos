from django.urls import path

from .views import TODOListAPIView

patterns = [
    path("", TODOListAPIView.as_view())
]