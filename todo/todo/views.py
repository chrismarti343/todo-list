from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    
    todo = Todo.objects.all()
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'todo': todo,
        'form': form
                }
    return render(request,'index.html', context)

def delete_todo(request, todo_id):
    event = Todo.objects.get(id=todo_id)
    event.delete()
    return redirect('/')

def complete_todo(request, todo_id):
    event = Todo.objects.get(id=todo_id)
    event.complete = True
    event.save()
    return redirect('/')

def undo_todo(request, todo_id):
    event = Todo.objects.get(id=todo_id)
    event.complete = False
    event.save()
    return redirect('/')

def update(request, todo_id):
        todo = Todo.objects.get(id=todo_id)
        
        form = TaskForm(instance=todo)

        if request.method == 'POST':
            form = TaskForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form':form}

        return render(request, 'update.html', context)


