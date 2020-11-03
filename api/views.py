from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import Taskserializer
from .models import Task

# Create your views here.

# all urls
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
    'list': '/task-list/',
    'Detail View': '/task-detail/<str:pk>/',
    'Create': '/task-create/',
    'Update': '/task-update/<str:pk>',
    'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)

# list of tasks
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = Taskserializer(tasks, many=True)
    return Response(serializer.data)

# detail task
@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id = pk)
    serializer = Taskserializer(task, many = False)
    return Response(serializer.data)

# Create a task
@api_view(['POST'])
def taskCreate(request):
    serializer = Taskserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update a task
@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = Taskserializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete a task
@api_view(['GET'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Item successfully Deleted")
