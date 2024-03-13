from django.shortcuts import render

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def index(request):
    return render(request, 'todos/index.html')
