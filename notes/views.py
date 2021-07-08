from django.views.generic import ListView, DetailView

from .models import Notebook


class NotebookListView(ListView):
    model = Notebook
    template_name = 'notes/notebook/listview.html'
    context_object_name = 'notebooks'


class NotebookView(DetailView):
    model = Notebook
    template_name = 'notes/notebook/notebookview.html'
    context_object_name = 'notebook'
