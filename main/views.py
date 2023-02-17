from main.models import Todo, User
# from rest_framework.views import APIView
from rest_framework.response import Response
# from django.forms import model_to_dict
from rest_framework import generics
from .serializer import TodotSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly # нужен для того чтоб записи были видны только для зарегистрированных польз-й


# Create your views here.

class TodolistView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodotSerializer
    permission_classes = [IsAuthenticated]

class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodotSerializer

class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodotSerializer

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodotSerializer

class TodoRetriveView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodotSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
