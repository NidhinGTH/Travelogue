from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from student.models import CustomUser

# Create your views here.


def userlogin(request):
    if (request.method == 'POST'):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('book:home')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')
# def register(request):
#     if request.method == 'POST':
#         u = request.POST.get('u', '')
#         p = request.POST.get('p', '')
#         c = request.POST.get('c', '')
#         e = request.POST.get('e', '')
#         f = request.POST.get('f', '')
#         l = request.POST.get('l', '')
#         pl = request.POST.get('pl', '')
#         num = request.POST.get('num', '')
#
#         # Check if the required fields are present
#         if u and p and c and e and f and l and pl and num:
#             if p == c:
#                 b = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l, place=pl, phone=num)
#                 return redirect('book:home')
#             else:
#                 return HttpResponse("Passwords are not the same")
#
#     return render(request, 'register.html')

def register(request):
        if (request.method == 'POST'):
            u = request.POST['u']
            p = request.POST['p']
            c = request.POST['c']
            e = request.POST['e']
            f = request.POST['f']
            l = request.POST['l']
            pl=request.POST['pl']
            num=request.POST['num']
            if(p==c):
                b = CustomUser.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l,place=pl,phone=num)
                b.save()
                return redirect('book:home')
            else:
                return HttpResponse("Passwords are not same")
        return render(request,'register.htpml')
@login_required
def user_logout(request):
    logout(request)
    return redirect('student:userlogin')

