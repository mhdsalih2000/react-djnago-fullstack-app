from django.urls import  path
from .views import  NoteDelete ,NoteListCreate

urlpatterns = [
    path('notes/',NoteListCreate.as_view(), name='List_create_notes'),
    path('notes/delete/<int:pk>/',NoteDelete.as_view(), name="delete_Note")
]
