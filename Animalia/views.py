from django.shortcuts import render
from .models import UserAnimalia

# Create your views here.

def index(request):
    usuario = UserAnimalia.objects.all()
    context = {"user": usuario}
    
    return render(request, "pages/index.html", context)


def signin(request):
    user = UserAnimalia.objects.all()
    context = {"user" : user}
    
    return render(request, 'pages/signin.html', context)