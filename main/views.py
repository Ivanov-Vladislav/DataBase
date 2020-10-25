from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .models import Task, Human
from .forms import TaskForm, HumanForm, CreateUserForm


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


class signUp(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'main/signUp.html', {'form': form})

    def post(self, request):
        bound_form = UserCreationForm(request.POST)

        if bound_form.is_valid():
            new_user = bound_form.save()
            return render(request, 'main/signIn.html')
        return render(request, 'main/signUp.html', {'form': bound_form})


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
