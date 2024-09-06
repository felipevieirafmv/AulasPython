from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request, 'home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.numero = request.POST.get("numero")
    novo_usuario.save()
    usuarios = {
        "usuarios": Usuario.objects.all()
    }
    return render(request, "usuarios.html", usuarios)
