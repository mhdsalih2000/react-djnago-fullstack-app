from django.shortcuts import render
from rest_framework import generics
from .Serializers import UserSerializer,NoteSerializer
from .models import Note
from django.contrib.auth.models import  User
from rest_framework.permissions import AllowAny,IsAuthenticated


# Create your views here.

class registerUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user   
        return Note.objects.filter(auther = user)

        
        

class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user   
        return Note.objects.filter(auther = user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(auther = self.request.user)
        else:
            print(serializer.error)
    