from django.shortcuts import render, redirect
from .models import Task
# Create your views here.

#Shows the list and enables adding tasks
def todo(request):
    #Shows tasks set by the user
    tasks = Task.objects.filter(user=request.user)
    if request.method == "POST":
        #Receives the input of the task name
        task_name = request.POST.get('task_name')
        if task_name:
            #Creates the task with the provided name
            Task.objects.create(user=request.user, task_name=task_name)
        return redirect('todo')
    return render(request, 'todo.html', {'tasks': tasks})

#Enables deletion of tasks
def task_delete(request, task_id):
    #Receives the name of the task
    task = Task.objects.get(id=task_id, user=request.user)
    if task:
        #Deletes the task
        task.delete()
    #Displays the to-do list without the deleted task
    return redirect('todo')