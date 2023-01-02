from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def userLogin(request):
    if request.method=='POST':
        username = request.POST['uname']
        password = request.POST['pass1']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('todouser:index')
    return render(request,'user_login/login.html')

def userLogout(request):
    logout(request)
    return redirect('todouser:login')
    

def userSignup(request):
    if request.method=='POST':
        username = request.POST['uname']
        email = request.POST['mail']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1==password2:
            user = User.objects.create_user(username,email,password1)
            user.save()
            return redirect('todouser:login')
    return render(request,'user_login/signup.html')
    

def index(request):
    if (request.user.is_authenticated):
        return render(request,'user_login/index.html')
    
    return redirect('todouser:login')
    