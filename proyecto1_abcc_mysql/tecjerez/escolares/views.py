from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Alumno

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

#==============ALTAS

class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    form = Alumno
    fields = '__all__'
    success_message = 'Alumbo agregado con EXITO'
    def get_success_url(self):
        return reverse('listar')
    
#==============BAJAS

class EliminarAlumno(SuccessMessageMixin, DeleteView):
    model = Alumno
    form = Alumno
    fields = '__all__'
    def get_success_url(self):
        success_message = 'Alumbo eliminado corretamente'
        messages.success(self.request, success_message)
        return reverse('listar')

#=============CAMBIOS    

class ModificarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    form = Alumno
    fields = '__all__'
    def get_success_message(self, cleaned_data):
        return reverse('listar')

#==============CONSULTAS

class DetallesAlumno(DetailView):
    model = Alumno

class ListarAlumnos(ListView):
    model = Alumno