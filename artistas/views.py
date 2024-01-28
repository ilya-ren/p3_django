from django.shortcuts import render
from .models import Artista, Genero
from django.http import HttpResponseRedirect
# Create your views here.



def index(request):
    artistas= Artista.objects.all()
    context={"artistas": artistas}
    return render(request, 'artistas/index.html', context)


def listadoSQL(request):
    artistas= Artista.objects.raw('SELECT * FROM artistas_artista')
    print(artistas)
    context={"artistas":artistas}
    return render(request, 'artistas/listadoSQL.html', context)

def crud(request):
    artistas= Artista.objects.all()
    context={'artistas': artistas}
    return render(request, 'artistas/artistas_list.html', context)

def artistasAdd(request):
    if request.method is not "POST":
        generos= Genero.objects.all()
        context={'generos':generos}
        return render(request, 'artistas/artistas_add.html', context)
    

