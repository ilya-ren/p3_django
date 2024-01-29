from django.shortcuts import render
from .models import Artista, Genero
from django.http import HttpResponseRedirect

from .forms import GeneroForm
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
    else:
        #en caso de ser POST se recuperan los datos del formulario y se graban en la tabla
        rut        = request.POST["rut"]
        nombre     = request.POST["nombre"]
        aPaterno   = request.POST["ap_paterno"]
        aMaterno   = request.POST["ap_materno"]
        fechaNac   = request.POST["fec_nacimiento"]
        genero     = request.POST["genero"]
        telefono   = request.POST["telefono"]
        email      = request.POST["email"]
        direccion  = request.POST["direccion"]
        activo=1

        objGenero= Genero.objects.get(id_genero= genero)
        obj= Artista.objects.create(rut=rut,
                                    nombre=nombre,
                                    ap_paterno=aPaterno,
                                    ap_materno=aMaterno,
                                    fec_nacimiento=fechaNac,
                                    id_genero=obj.genero,
                                    telefono=telefono,
                                    email=email,
                                    direccion=direccion,
                                    activo=1)
        obj.save()
        context={'mensaje':"Datos grabados con exito!"}
        return render(request, 'artistas/artistas_add.html', context)
    

def artistas_del(request,pk):
    context={}
    try:
        artista= Artista.objects.get(rut=pk)

        artista.delete()
        mensaje = "Registro del artista eliminado con exito."
        artista = Artista.objects.all()
        context= {'artistas': artistas, 'mensaje': mensaje}
        return render(request, 'artistas/artistas_list.html', context)
    except:
        mensaje= "No existe artista registrado con ese rut."
        artistas= Artista.objects.all()
        context= {'artista': artistas, 'mensaje': mensaje}
        return render(request, 'artista/artistas_list.html', context)
    
def artistas_finEdit(request, pk):
    if pk != "":
        artista= Artista.objects.get(rut=pk)
        generos= Genero.objects.all()

        print(type(artista.id_genero.genero))

        context={'artista': artista, 'generos':generos}
        if artista:
            return render(request, 'artistas/artistas_edit.html', context)
        else:
            context={'mensaje': "Error, el rut no existe."}
            return render (request, 'artistas/artistas_list.html', context)
        
def artistasUpdate(request):
    if request.method == "POST":
        rut       = request.POST["rut"]
        nombre    = request.POST["nombre"]
        aPaterno  = request.POST["ap_paterno"]
        aMaterno  = request.POST["ap_materno"]
        fechaNac  = request.POST["fechaNac"]
        genero    = request.POST["genero"]
        telefono  = request.POST["telefono"]
        email     = request.POST["email"]
        direccion = request.POST["direccion"]
        activo    = "1"

        objGenero= Genero.objects.get(id_genero= genero)

        artista= artista()
        artista.rut= rut
        artista.nombre= nombre
        artista.ap_paterno= aPaterno
        artista.ap_materno= aMaterno
        artista.fechaNac= fechaNac
        artista.id_genero=objGenero
        artista.telefono= telefono
        artista.email=email
        artista.direccion=direccion
        artista.activo=1
        artista.save()

        generos=Genero.objects.all()
        context={'mensaje': "Datos del artista actualizados.", 'generos': generos, 'artista': artista}
        return render(request, 'artistas/artistas_edit.html', context)
    

    else:
        artistas = Artista.objects.all()
        context={'artistas': artistas}
        return render(request, 'artistas/artistas_list.html', context)
    
def crud_generos(request):
    generos= Genero.objects.all()
    context={'generos': generos}
    print("Enviando datos a generos_list")
    return render(request,"artistas/generos_list.html", context)


def generosAdd(request):
    print("Te encuentras en el controlador para agregar Género")
    context={}

    if request.method=="POST":
        print("controlador es un post...")
        form= GeneroForm(request.POST)
        if form.is_valid:
            print("agregar, is_valid")
            form.save()

            #limpiarform
            form=GeneroForm()

            context={'mensaje': "Datos guardados con exito", "form":form}
            return render(request, 'artistas/generos_add,html', context)
    else:
        form= GeneroForm()
        context={'form': form}
        return render(request, 'artistas/generos_add.html', context)

def generos_del(request, pk):
    mensajes=[]
    errores=[]
    generos= Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Hecho. Datos eliminados...")
            context= {'generos': generos, 'mensajes': mensajes, 'errores': errores}
            return render(request, 'artistas/generos_list.html', context)
    except:
        print("Error, el id ingresado no existe.")
        generos=Genero.objects.all()
        mensaje= "Error, el id ingresado no existe."
        context={'mensaje': mensaje, 'generos': generos}
        return render(request, 'artistas/generos_list.html', context)
    
def generos_edit(request,pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Se encontro el género a editar")
            if request.method=="POST":
                print("edit, es un post")
                form= GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje= "Dato actualizado con exito"
                print(mensaje)
                context= {'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'artistas/generos_edit.html', context)
            else: 
                #metodo no es POST
                print("edit NO es un POST")
                form=GeneroForm(instance=genero)
                mensaje=""
                context={'genero': genero, 'form': form, 'mensaje': mensaje}
                return render(request, 'artistas/generos_edit.html', context)
    except:
        print("Error, el género a editar no existe.")
        generos=Genero.objects.all()
        mensaje= "Erros, el género a editar no existe."
        context= {'mensaje': mensaje, 'generos': generos}
        return render(request, 'artistas/generos_list.html, context')
        
        


        

    

