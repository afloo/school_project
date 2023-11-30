from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from store.models import Department


# Create your views here.
def index(request):
    return render(request,"home.html")


def login(request):
    if request.method== 'POST':
        username=request.POST['USERNAME']
        password = request.POST['PASSWORD']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def register(request):
    if request.method== 'POST':
        username=request.POST['USERNAME']
        password = request.POST['PASSWORD']
        cpassword = request.POST['CONFIRM PASSWORD']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('register')

            user = User.objects.create_user(username=username, password=password,)

            user.save();

            return redirect('login')
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('')
    return render(request, "register.html")

def form(request):

    return render(request,"form.html")

def order(request):
    return render(request,'order.html')


def allDpt(request):
    subjects = Department.objects.all()
    return render(request, 'index.html', {'subjects': subjects})