from django.shortcuts import render, redirect
from .models import Task, Human
from .forms import TaskForm, HumanForm

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def tasks(request):
    tasks = Task.objects.all()
    humans = Human.objects.all()
    return render(request, 'main/tasks.html', {'tasks': tasks, 'humans': humans})

def signIn(request):
    return render(request, 'main/signIn.html')

def createtask(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверная'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createtask.html', context)

def createhuman(request):
    error = ''
    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверная'

    form = HumanForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createhuman.html', context)
