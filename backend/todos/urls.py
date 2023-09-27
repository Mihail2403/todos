from django.urls import path
from .views import DeleteTODOAPIView
from .views import TODOListAPIView

patterns = [
    path("", TODOListAPIView.as_view()),
    path("delete/", DeleteTODOAPIView.as_view())
]