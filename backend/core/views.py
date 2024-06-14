from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, CategorySerializer, ToDoSummarySerializer, CategoryDetailSerializer
from .models import Todo, Category

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
 
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update"):
            return CategorySerializer
        return CategoryDetailSerializer 
