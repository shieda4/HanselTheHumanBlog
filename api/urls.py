from django.urls import path
from .views import NotebookAPIListView, NoteAPIRetrieveView, NotebookAPIRetrieveView

urlpatterns = [
    path('notebooks/', NotebookAPIListView.as_view(), name='notebooks_api'),
    path('notebooks/<slug:slug>/', NotebookAPIRetrieveView.as_view(), name='notebook_api'),
    path('notebooks/notes/<uuid:pk>', NoteAPIRetrieveView.as_view(), name='notes_api'),
]
