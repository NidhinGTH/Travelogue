from django.db.models import Q
from book.forms import bookform
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# function based
from django.http import HttpResponse


# Create your views here.
from django.http import HttpResponse
from book.models import book
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html')

@login_required
def add(request):
    return render(request, 'add.html')

@login_required
def view(request):
    k = book.objects.all()
    return render(request, 'view.html', context={'b': k})

@login_required
def add(request):
    if (request.method == "POST"):  # After form submission

        t = request.POST['t']
        a = request.POST['a']

        p = request.POST['p']
        f = request.FILES['f']
        c = request.FILES['c']

        b = book.objects.create(title=t, author=a, price=p, pdf=f, cover=c)

        b.save()
        return view(request)

    return render(request, 'add.html')

@login_required
def add1(request):
    if (request.method == "POST"):
        form = bookform(request.POST)
        if form.id_valid():
            form.save()
            return view(request)
    form = bookform()
    return render(request, 'addbooks1.html', {'form': form})

@login_required
def fact(request):
    if (request.method == "POST"):
        num = int(request.POST['n'])
        # return HttpResponse(num)
        # factorial--1*2*3*...num
        f = 1
        for i in range(1, num + 1):
            f = f * i
        return render(request, 'fact.html', {'fact': f})

    return render(request, 'fact.html')


# views.py inside the book module
@login_required
def details(request,p):
    b = book.objects.get(id=p)
    return render(request, 'details.html', {'b': b})


# views.py inside the book module
@login_required
def edit(request,p):
    b=book.objects.get(id=p)
    if (request.method == "POST"):
        form = bookform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return view(request)
    form=bookform(instance=b)
    return render(request,'edit.html',{'form':form})
@login_required
def search(request):
    b = None
    q = ""
    if(request.method == "POST"):
        q = request.POST['q']
        b = book.objects.filter(Q(title__icontains=q)| Q(author__icontains=q))
    return render(request,'search.html',{'q':q,'b':b})


# views.py inside the book module
@login_required
def delete(request,p):
    b = book.objects.get(id=p)
    b.delete()
    return view(request)