from django.shortcuts import render
from travelapp.models import Place
from travelapp.models import Team


# Create your views here.
def home(request):
    p = Place.objects.all()
    t=Team.objects.all()
    return render(request, 'home.html', {'p': p,'t':t})

def search(request):
    p= None
    t = ""

    if request.method == "POST" or request.method == "GET":
        q = request.POST.get('p') or request.GET.get('t')
        p= Place.objects.filter(p(name__icontains=q) | p(desc__icontains=q))

    return render(request, 'search.html', {'p': p, 't': t})
