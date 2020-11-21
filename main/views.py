from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Task
from .forms import TaskForm, CreateUserForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'main/tasks.html', {'tasks': tasks})


def signIn(request):
    return render(request, 'main/registration/signIn.html')


class signUp(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'main/registration/signUp.html', {'form': form})

    def post(self, request):
        bound_form = CreateUserForm(request.POST)

        if bound_form.is_valid():
            new_user = bound_form.save()
            return render(request, 'main/registration/signIn.html')
        return render(request, 'main/registration/signUp.html', {'form': bound_form})


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