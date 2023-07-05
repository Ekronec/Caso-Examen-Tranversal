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

def Bird(request):
    usuario = UserAnimalia.objects.all()
    context = {"user": usuario}
    return render(request, "pages/Bird.html", context)

def signin(request):
    if request.method != "POST":
        user = UserAnimalia.objects.all()
        context = {"user" : user}
        return render(request, 'pages/signin.html', context)
    else:
        emailUsuario = request.POST["emailUsuario"] 
        nameUsuario = request.POST["nameUsuario"]
        lastName = request.POST["lastName"]
        password = request.POST["password"] 
        region = request.POST["region"]
        provincia = request.POST["provincia"]
        comuna = request.POST["comuna"]
        address = request.POST["address"]
    
    objUser = UserAnimalia.objects.create(
        emailUsuario = emailUsuario,
        nameUsuario = nameUsuario,
        lastName = lastName,
        password = password,
        region = region,
        provincia = provincia,
        comuna = comuna,
        address = address,
        activo = 1,
    )
    objUser.save()
    context = {"mensaje" : "OK Usuario Registrado"}
    return(request, "pages/signin.html", context)




