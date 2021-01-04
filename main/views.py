from django.shortcuts import render, redirect
from .models import Task1, Human, status
from .forms import Task1Form, HumanForm
import datetime

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def tasks(request):
    tasks = Task1.objects.all()
    humans = Human.objects.all()
    Status = status.objects.all()
    return render(request, 'main/tasks.html', {'title': 'Главная', 'tasks': tasks, 'humans': humans, 'Status':Status})

def createtask(request):
    if not(str(request.user) == 'AnonymousUser'):
        error = ''
        if request.method == 'POST':
            form = Task1Form(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_person = request.user
                date_now = str(datetime.datetime.now())
                post.date = date_now[0:10]
                post.id_performing_person = "Свободна для выполнения"
                post.save()
                return redirect('home')
            else:
                error = 'Форма неверная'

        form = Task1Form()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'main/createtask.html', context)
    else:
        return redirect('accounts/login/')

def id_performing_personTodo(request, todo_id):
    if not (str(request.user) == 'AnonymousUser'):
        todo = Task1.objects.get(pk=todo_id)
        user_name = request.user
        todo.id_performing_person = str(user_name)
        todo.save()
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('tasks')

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
    form.ages = '!!'
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createhuman.html', context)
