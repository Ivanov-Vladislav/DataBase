from django.shortcuts import render, redirect
from .models import Task1, Human, status, branch
from .forms import Task1Form, HumanForm
import datetime

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def tasks(request):
    humans = Human.objects.all()
    humas_auth_bool = False
    for human in humans:
        if (str(human.id_registarion) == str(request.user.id)):
            humas_auth_bool = True
            break
    if humas_auth_bool == False:
        return redirect('createhuman')
    tasks = Task1.objects.all()
    user_info =  str(request.user)
    return render(request, 'main/tasks.html', {'title': 'Задачи', 'tasks': tasks, 'user_info':user_info})

def createtask(request):
    Status = status.objects.all()
    humans = Human.objects.all()
    humas_auth_bool = False
    for human in humans:
        if (str(human.id_registarion) == str(request.user.id)):
            humas_auth_bool = True
            break
    if humas_auth_bool == False:
        return redirect('createhuman')
    if not(str(request.user) == 'AnonymousUser'):
        error = ''
        if request.method == 'POST':
            form = Task1Form(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_person = request.user
                date_now = str(datetime.datetime.now())
                post.date = date_now[0:10]
                post.id_performing_person = "-"
                post.id_status = "Свободно"
                post.save()
                return redirect('tasks')
            else:
                error = 'Форма неверная'

        form = Task1Form()
        context = {
            'form': form,
            'error': error,
            'Status': Status,
        }
        return render(request, 'main/createtask.html', context)
    else:
        return redirect('accounts/login/')

def id_up_status(request, todo_id, cancel = False):
    if not (str(request.user) == 'AnonymousUser'):
        humans = Human.objects.all()
        Status = status.objects.all()

        humas_auth_bool = False
        for human in humans:
            if (str(human.id_registarion) == str(request.user.id)):
                humas_auth_bool = True
                break
        if humas_auth_bool == False:
            return redirect('createhuman')

        todo = Task1.objects.get(pk=todo_id)
        if (str(todo.id_performing_person) == str(request.user)) or (str(todo.id_status) == str(Status[0])):
            user_name = request.user
            el_index = 0
            for el in Status:
                if str(todo.id_status) == str(el):
                    break
                el_index += 1
            todo.id_status = str(Status[el_index+1])
            todo.id_performing_person = str(user_name)
            todo.save()
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('tasks')

def id_down_status(request, todo_id, cancel = False):
    if not (str(request.user) == 'AnonymousUser'):
        humans = Human.objects.all()
        Status = status.objects.all()

        humas_auth_bool = False
        for human in humans:
            if (str(human.id_registarion) == str(request.user.id)):
                humas_auth_bool = True
                break
        if humas_auth_bool == False:
            return redirect('createhuman')

        todo = Task1.objects.get(pk=todo_id)
        if str(todo.id_performing_person) == str(request.user):
            user_name = request.user
            el_index = 0
            for el in Status:
                if str(todo.id_status) == str(el):
                    break
                el_index += 1
            todo.id_status = str(Status[el_index-1])
            if str(todo.id_status) == str(Status[0]):
                todo.id_performing_person = '-'
            else:
                todo.id_performing_person = str(user_name)
            todo.save()
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('tasks')

def createhuman(request):
    error = ''
    Branch = branch.objects.all()
    if not (str(request.user) == 'AnonymousUser'):
        if request.method == 'POST':
            form = HumanForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_registarion = request.user.id
                post.save()
                return redirect('tasks')
            else:
                error = 'Форма неверная'

        form = HumanForm()
        context = {
            'form': form,
            'error': error,
            'Branch': Branch
        }
        return render(request, 'main/createhuman.html', context)
