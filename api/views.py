from rest_framework.generics import ListAPIView, RetrieveAPIView
from notes.models import Notebook, Note
from .serializers import NotebookListViewSerializer, NoteSerializer, NotebookRetrieveViewSerializer


class NotebookAPIListView(ListAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookListViewSerializer


class NotebookAPIRetrieveView(RetrieveAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookRetrieveViewSerializer
    lookup_field = 'slug'


class NoteAPIRetrieveView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
