from django.shortcuts import render, redirect
from .models import Task1, Human, status, branch, Avatar, team, team_person
from .forms import Task1Form, HumanForm, AvatarForm, Team_Person_Form
from django.db.models import Q
import datetime
import os
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')

def tasks(request, order_like='title'):
    search_query = request.GET.get('search', '')
    order_like = request.GET.get('order_like', '')

    try:
        if search_query:
            task_list = Task1.objects.filter(Q(title__icontains = search_query) | Q(description__icontains = search_query)
                                             | Q(date__icontains = search_query) | Q(id_person__icontains = search_query)
                                             | Q(id_status = search_query)
                                             | Q(id_performing_person__icontains = search_query))
        else:
            task_list = Task1.objects.all()
    except ValueError:
        task_list = []

    if order_like:
        task_list = task_list.order_by(order_like)

    self_person = Human.objects.get(id_registarion=request.user.id)
    team_persons = team_person.objects.get(id_person = self_person)

    #for el in task_list:

    #    team_creator = team_person.objects.get(id_person = el.id_person)
    #    if team_creator.id_team == team_persons.id_team:
    #        print("!")


    Status_good = status.objects.get(id=3)
    Status_norm = status.objects.get(id=2)
    if not(str(request.user) == "AnonymousUser"):
        if str(Human.objects.filter(id_registarion=request.user.id)) == "<QuerySet []>":
            return redirect('createhuman')

    paginator = Paginator(task_list, 10)

    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

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
        teams = team.objects.all()
        print(teams)
        if request.method == 'POST':
            form = HumanForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.id_branch = branch.objects.get(name = request.POST.get("id_branch"))
                post.id_registarion = request.user.id
                post.save()


                return redirect('/create_person_team')
            else:
                error = 'Форма неверная'

        form = HumanForm()
        context = {
            'form': form,
            'error': error,
            'Branch': Branch,
            'teams':teams,
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


def edit_avatar(request):
    error = ''
    human_temp = Human.objects.get(id_registarion=request.user.id)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            human = form.save(commit=False)
            human_temp.avatar = human.avatar
            human_temp.save()
            return redirect('profile')
        else:
            error = 'Форма неверная'

    form = HumanForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/edit_avatar.html', context)


def edit_data(request):
    try:
        Branch = branch.objects.all()
        human = Human.objects.get(id_registarion=request.user.id)
        if request.method == "POST":
            human.first_name = request.POST.get("first_name")
            human.second_name = request.POST.get("second_name")
            self_branch = request.POST.get("id_branch")
            human.id_branch = branch.objects.get(name = self_branch)
            print(human.id_branch)
            human.save()
            return HttpResponseRedirect("/profile")
        else:
            return render(request, "main/edit_data.html", {'title': 'Редактирование профиля', "human": human, 'Branch': Branch})
    except human.DoesNotExist:
        return HttpResponseNotFound("<h2>Human not found</h2>")

def create_person_team(request):
    error = ''

    if not (str(request.user) == 'AnonymousUser'):
        teams = team.objects.all()
        #print(teams)
        if request.method == 'POST':

            form = Team_Person_Form()
            post = form.save(commit=False)
            post.id_team = team.objects.get(name=request.POST.get("id_team"))
            post.id_person = Human.objects.get(id_registarion=request.user.id)
            print(post)
            post.save()


            return redirect('tasks')

        context = {
            'teams': teams,
        }
        return render(request, 'main/create_person_team.html', context)