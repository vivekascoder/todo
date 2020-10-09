from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from app.models import Todo
from app.forms import StudentForm, TodoForm

def home(request):
    todos = Todo.objects.all()
    data = {
        'todos': todos,
    }
    return render(request, "index.html", context=data)

def todo_display(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return HttpResponse(f"<h1>Wrong, Primary Key. {pk}</h1>")
    return render(request, 'display_todo.html', context={'todo': todo})


def todo_update(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return HttpResponse(f"<h1>Wrong, Primary Key. {pk}</h1>")

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = TodoForm(instance=todo)
    return render(request, 'update_todo.html', context={'form': form})

def todo_create(request):
    if request.method == "GET":
        form = TodoForm()
        return render(request, 'create_todo.html', context={'form': form})
    elif request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return HttpResponse("Form is not valid.")

def todo_delete(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return HttpResponse(f"<h1>Wrong, Primary Key. {pk}</h1>")
    todo.delete()
    return redirect("home")


# Step-1: CTRL + SHIFT + P
# User Snippets

class HomeView(View):
    def get(self, request):
        pass
    

