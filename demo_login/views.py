from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Todo
# Create your views here.
def userlogin(request):
    if request.method=='POST':
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
        user = authenticate(username=uname,password=pass1)
        if user:
            login(request,user)
            return redirect('demo_login:home')
    return render(request,'demo_login/login.html')
    

def userlogout(request):
    logout(request)
    return redirect('demo_login:login')
    

def usersignup(request):
    if request.method=='POST':
        uname = request.POST['uname']
        email = request.POST['mail']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if(pass1==pass2):
            user = User.objects.create_user(uname,email,pass1)
            user.save()
            return redirect('demo_login:login')
    return render(request,'demo_login/signup.html',{})


def home(request):
    try:
        if(request.user.is_authenticated):
            print(1)
            return render(request,'demo_login/home.html',{'todo_list':request.user.todo_set.all()})
        return redirect('demo_login:login')
    except:
        return redirect('demo_login:login')


def index(request):
    return render(request,'demo_login/index.html')

def add(request):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['desc']
        todo = Todo(title=title,description=description,user=request.user)
        todo.save()
        return redirect('demo_login:home')
    return redirect('demo_login:index')

def update(request,id):
    if request.method=='POST':
        title = request.POST['title']
        description = request.POST['desc']
        todo = Todo.objects.get(pk=id)
        todo.title=title
        todo.description=description
        todo.save()
        return redirect('demo_login:home')
    todo = Todo.objects.get(pk=id)
    return render(request,'demo_login/update.html',{'todo':todo})

def delete(request,id):
    todo = Todo.objects.get(pk=id)
    todo.delete()
    return redirect('demo_login:home')

def modal(request):
    return render(request,'demo_login/modal.html')