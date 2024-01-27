from django.shortcuts import render

from .models import Artista, Genero
# Create your views here.



def index(request):
    artistas= Artista.objects.all()
    context={"artistas": artistas}
    return render(request, 'artistas/index.html', context)