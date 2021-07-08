from django.urls import path

from .views import NotebookListView, NotebookView

urlpatterns = [
    path('notebooks/', NotebookListView.as_view(), name='notebooks'),
    path('<slug:slug>/', NotebookView.as_view(), name='notebook'),
]
