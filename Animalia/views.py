from django.shortcuts import render
from .models import UserAnimalia

# Create your views here.

def index(request):
    usuario = UserAnimalia.objects.all()
    context = {"user": usuario}
    
    return render(request, "pages/index.html", context)

def login(request):
    usuario = UserAnimalia.objects.all()
    context = {"user": usuario}
    
    return render(request, "pages/login.html", context)

def Dog(request):
    usuario = UserAnimalia.objects.all()
    context = {"user": usuario}
    
    return render(request, "pages/Dog.html", context)

def Cat(request):
    usuario = UserAnimalia.objects.all()
    context = {"user": usuario}
    
    return render(request, "pages/Cat.html", context)

def aquatic(request):
    usuario = UserAnimalia.objects.all()
    context = {"user": usuario}
    
    return render(request, "pages/aquatic.html", context)


def signin(request):
    user = UserAnimalia.objects.all()
    context = {"user" : user}
    
    return render(request, 'pages/signin.html', context)


