from django.shortcuts import render, HttpResponse
from django.views import View
from app.models import Todo


def home(request):
    todos = Todo.objects.all()
    data = {
        'todos': todos,
        'name': "Vivek"
    }
    return render(request, "index.html", context=data)