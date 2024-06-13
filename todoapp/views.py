from django.shortcuts import get_object_or_404, redirect, render

from todoapp.forms import TodoForm
from .models import Todo

# Create your views here.
def home(request):
    todos = Todo.objects.filter(Status=False)
    completed = Todo.objects.filter(Status=True)
    if request.method == "POST":
        task = request.POST.get('task')
        desc = request.POST.get('description')
        priority = request.POST.get('priority')
        new_todo = Todo(Task=task,Description=desc,Priority=priority)
        new_todo.save()
    return render(request,'todo_home.html',{'todos':todos,'completed':completed})

def complete_todo(request, id):
    todo = get_object_or_404(Todo,id=id)
    todo.Status = True
    todo.save()
    return redirect('home')

def delete_todo(request, id):
    todo = get_object_or_404(Todo,id=id)
    todo.delete()
    return redirect('home')

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.Task = request.POST.get('task')
        todo.Description = request.POST.get('description')
        todo.Priority = request.POST.get('priority')
        todo.save()
        return redirect('home')        
    return render(request, 'edit_todo.html', {'todo': todo})