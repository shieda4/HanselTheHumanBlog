from rest_framework.serializers import ModelSerializer
from notes.models import Notebook, Note


class NotebookListViewSerializer(ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('id', 'title', 'slug')


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'date', 'notebook', 'content')


class NotebookRetrieveViewSerializer(ModelSerializer):
    class Meta:
        model = Notebook
        fields = ('id', 'title', 'notes')
