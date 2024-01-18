from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import render
from .forms import UserForm


class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer


def index(request):
	data = {"variable": "Hello!!!"}
	return render(request, "index.html", context=data)


def add_task(request):
	if request.method == "POST":
		name = request.POST.get("name")
		desc = request.POST.get("desc")
		# return f"Привет, {name}, твой возраст: {age}"
		return HttpResponse(f"<h2>Название, {name}, Описание: {desc}</h2>")
	else:
		userform = UserForm()
		return render(request, "add_task.html", {"form": userform})
