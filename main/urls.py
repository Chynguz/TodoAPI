from django.urls import path
from main.views import TodolistView, TodoCreateView, TodoDeleteView, TodoUpdateView, TodoRetriveView, UserCreate


urlpatterns = [
    path('api/', TodolistView.as_view()),
    path('update/<int:pk>', TodoUpdateView.as_view()),
    path('create/<int:pk>', TodoCreateView.as_view()),
    path('delete/<int:pk>', TodoDeleteView.as_view()),
    path('retrive/<int:pk>', TodoRetriveView.as_view()),
    path('usercreate/', UserCreate.as_view()),
]