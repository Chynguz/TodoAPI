from rest_framework.serializers import ModelSerializer
from .models import Todo, User
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

class TodotSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'created')

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','age','email','password',)


class SignUpSerializer(ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}
    )
    class Meta:
      model = User
      fields = ('first_name', 'last_name', 'age', 'email', 'password')