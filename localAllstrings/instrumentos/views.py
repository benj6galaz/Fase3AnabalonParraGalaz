from django.shortcuts import render
from .models import Instrumento


# Create your views here.
def index(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_instrumentos': num_instrumentos},
    )

def Login(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'Login.html',
        context={'num_instrumentos': num_instrumentos},
    )

def Registrar(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'Registrar.html',
        context={'num_instrumentos': num_instrumentos},
    )

def Precios(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'Precios.html',
        context={'num_instrumentos': num_instrumentos},
    )    

def Compra(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'Compra.html',
        context={'num_instrumentos': num_instrumentos},
    )  

def Guitarras(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'Guitarras.html',
        context={'num_instrumentos': num_instrumentos},
    ) 
    
def Bajos(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'Bajos.html',
        context={'num_instrumentos': num_instrumentos},
    )    

def Formulario(request):
    num_instrumentos = Instrumento.objects.all().count()

    return render(
        request,
        'Formulario.html',
        context={'num_instrumentos': num_instrumentos},
    )   
                  


# CRUD.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

class InstrumentoCreate(CreateView):
    model = Instrumento
    fields = ['id', 'nombre', 'descripcion']

class InstrumentoUpdate(UpdateView):
    model = Instrumento
    fields = ['id','nombre', 'descripcion']

class InstrumentoDelete(DeleteView):
    model = Instrumento
    success_url = reverse_lazy('index')

class InstrumentoDetailView(generic.DetailView):
    model = Instrumento
 
class InstrumentoListView(generic.ListView):   
     model = Instrumento
     paginate_by = 20