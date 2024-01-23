from django.http import Http404
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def index(request):
    tasks = Task.objects.all()
    data = {"variable": "Hello!!!", "tasks": tasks}
    return render(request, "index.html", context=data)


def add_task(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        userform = TaskForm()
        return render(request, "add_task.html", {"form": userform})


def edit_task(request, id):  
    try:
        old_data = get_object_or_404(Task, id=id)
    except Exception:
        raise Http404('Такой задачи не существует')
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=old_data)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        outperform = TaskForm(instance=old_data)
        return render(request, "edit_task.html", {"form": outperform})
    
    
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    except Exception:
        raise Http404('Такой задачи не существует')
