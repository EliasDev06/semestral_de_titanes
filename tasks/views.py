from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
from .forms import TaskFrom
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar ususario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm, 'error': 'Usuario ya existe'})
        return render(request, 'signup.html', {
            'form': UserCreationForm, 'error': 'Contraseñas no coinsiden'})

@login_required
def tasks(request):#muestra las tareas  (las tareas no completadas)
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True).order_by('-datecompleted')
    return render(request, 'tasks.html', {'tasks':tasks})

@login_required
def tasks_complete (request):#muestra las tareas completadas
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request, 'tasks.html', {'tasks':tasks})

@login_required
def task_detailt(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk = task_id)
        form = TaskFrom(instance=task)
        return render(request, 'task_detail.html',{'task':task, 'form':form})
    else:
        try:
            task = get_object_or_404(Task, pk = task_id, user=request.user)
            form = TaskFrom(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except:
            return render(request, 'task_detail.html',
                          {'task':task, 'form':form,'error':'Error actualizando'})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task (request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
    
@login_required
def signot(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], 
                     password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña son incorrectos'
            })
        else:
            #si se encuentra el usuario, lo guardamos con el login y lo 
            # redirecionamos

            login(request, user)
            return redirect('tasks')

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
                'form':TaskFrom  })
    else:
       try:
            form = TaskFrom(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user 
            new_task.save()
            print(new_task)
            return redirect('tasks')
       except ValueError:
            return render(request, 'create_task.html', {
                'form':TaskFrom,  
                'error':'Ingresa datos validos'})
    