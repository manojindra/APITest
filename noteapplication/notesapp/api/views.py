from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from notesapp.api.serializers import NoteSerializer
from notesapp.models import Note

class NotesListView(ListCreateAPIView):
    serializer_class = NoteSerializer    
    queryset = Note.objects.all()
    """def get_queryset(self):

        if self.request.user.is_authenticated:
            return Note.objects.filter(user=self.request.user.userid)
        
        return Note.objects.none()"""


class NotesDetailedView(RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    lookup_field = 'noteId'

