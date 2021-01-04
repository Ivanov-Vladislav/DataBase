from django.shortcuts import render, redirect
from .models import Task1, Human
from .forms import Task1Form, HumanForm
import datetime

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def tasks(request):
    tasks = Task1.objects.all()
    humans = Human.objects.all()
    return render(request, 'main/tasks.html', {'title': 'Главная', 'tasks': tasks, 'humans': humans})

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
