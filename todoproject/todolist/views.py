from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import render, redirect
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
