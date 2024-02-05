# your_app/views.py
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from app1.models import CustomUser

def home(request):
    return render(request, 'home.html')
def adminsignup (request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        pl = request.POST['pl']
        n = request.POST['n']
        if (p == c):
            a = CustomUser.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l, place=pl,
                                               phone=n)
            a.is_admin = True
            a.save()
            return home(request)
        else:
            return HttpResponse("passwords are not same")

    return render (request,  'adminsignup.html')

def studentsignup (request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        pl = request.POST['pl']
        n = request.POST['n']
        if (p == c):
            a = CustomUser.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l, place=pl,
                                               phone=n, )
            a.is_student = True
            a.save()
            return home(request)
        else:
            return HttpResponse("passwords are not same")

    return render(request, 'studentsignup.html')

def teachersignup (request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        c = request.POST['c']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        pl = request.POST['pl']
        n = request.POST['n']
        if (p == c):
            a = CustomUser.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l, place=pl,
                                               phone=n)
            a.is_teacher = True
            a.save()
            return home(request)
        else:
            return HttpResponse("passwords are not same")

    return render (request,  'teachersignup.html')

def adminhome (request):
    return render (request,'adminhome.html')
def studenthome (request):
    return render (request,'studenthome.html')
def teacherhome (request):
    return render (request,'teacherhome.html')


def userlogin(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.is_admin==True:
            login(request,user)
            return adminhome(request)
        elif user and user.is_student==True:
            login(request,user)
            return studenthome(request)

        elif user and user.is_teacher==True:
            login(request,user)
            return teacherhome(request)

        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('app1:userlogin')