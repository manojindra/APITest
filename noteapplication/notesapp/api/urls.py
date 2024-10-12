from rest_framework.urls import path
from notesapp.api.views import NotesListView, NotesDetailedView

urlpatterns = [
    path('',NotesListView.as_view()),
    path('<int:noteId>/', NotesDetailedView.as_view()),
    
]