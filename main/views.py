from django.shortcuts import render, redirect
from .models import Task1, Human, status, branch
from .forms import Task1Form, HumanForm
import datetime
import os
from django.http import HttpResponseRedirect, HttpResponseNotFound

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def tasks(request):
    humans = Human.objects.all()
    Status_good = status.objects.get(id=3)
    Status_norm = status.objects.get(id=2)
    humas_auth_bool = False
    if not(str(request.user) == "AnonymousUser"):
        for human in humans:
            if (str(human.id_registarion) == str(request.user.id)):
                humas_auth_bool = True
                break
        if humas_auth_bool == False:
            return redirect('createhuman')
    tasks = Task1.objects.all()

    user_info = str(request.user)
    return render(request, 'main/tasks.html', {'title': 'Задачи', 'tasks': tasks, 'user_info':user_info, 'Status_good':Status_good, 'Status_norm':Status_norm})

def createtask(request):
    Status = status.objects.all()
    humans = Human.objects.all()
    humas_auth_bool = False
    if not (str(request.user) == "AnonymousUser"):
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
                post.id_status = Status[0]
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
            todo.id_status = Status[el_index+1]
            todo.id_performing_person = str(user_name)
            todo.save()
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('profile')

def id_down_status(request, todo_id):
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
            todo.id_status = Status[el_index-1]
            if str(todo.id_status) == str(Status[0]):
                todo.id_performing_person = '-'
            else:
                todo.id_performing_person = str(user_name)
            todo.save()
    else:
        return redirect('http://127.0.0.1:8000/accounts/login/')

    return redirect('profile')

def createhuman(request):
    error = ''
    Branch = branch.objects.all()
    Human.objects.filter(id_registarion=request.user.id).delete()
    if not (str(request.user) == 'AnonymousUser'):
        if request.method == 'POST':
            form = HumanForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_branch = branch.objects.get(name = request.POST.get("id_branch"))
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

def profile(request):
    try:
        user_info = request.user
        Status_good = status.objects.get(id=3)
        Status_norm = status.objects.get(id=2)
        tasks = Task1.objects.all()
        humans = Human.objects.all()
        for human in humans:
            if str(human.id_registarion) == str(user_info.id):
                self_human = human
        user_info = str(request.user)
        return render(request, 'main/profile.html', {'title': 'Профиль', 'tasks':tasks, 'self_human': self_human, 'user_info':user_info,  'Status_good':Status_good, 'Status_norm':Status_norm})
    except ValueError:
        return redirect('createhuman')
    except UnboundLocalError:
        return redirect('createhuman')
def delete_task(request, id):
    task = Task1.objects.get(pk=id)
    task.delete()
    return redirect('tasks')


def edit(request, id):
    try:
        todo = Task1.objects.get(id=id)
        if request.method == "POST":
            todo.title = request.POST.get("title")
            todo.description = request.POST.get("description")
            todo.save()
            return HttpResponseRedirect("/tasks")
        else:
            return render(request, "main/edit.html", {'title': 'Профиль', "todo": todo})
    except todo.DoesNotExist:
        return HttpResponseNotFound("<h2>Todo not found</h2>")
