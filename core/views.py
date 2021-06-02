from core.models import Todo
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

# Create your views here.


def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/index')
        else:
            return redirect('/')
    return render(request,'accounts/login.html')

def userSignUp(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['con_password']
        if pass1 == pass2:
            new_user = User(email=email,username=username,password=make_password(pass1))
            new_user.save()
            return redirect('/')
        else:
            return redirect('/signup')
    return render(request,'accounts/signup.html')

def userLogout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def index(request):
    todo = Todo.objects.filter(user=request.user)
    if request.method == 'POST':
        new_todo = Todo(user=request.user,title=request.POST['title'])
        new_todo.save()
        return redirect('/index')
    return render(request,'index.html',{'todos':todo})


def deleteTask(reqest,pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/index')