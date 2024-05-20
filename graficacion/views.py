from django.shortcuts import render




# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Applicant, ApplicantExperience
from graficacion.graficas import *

class ApplicantListView(ListView):
    model = Applicant
    template_name = 'applicant_list.html'

class ApplicantDetailView(DetailView):
    model = Applicant
    template_name = 'applicant_detail.html'

class ApplicantCreateView(CreateView):
    model = Applicant
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    template_name = 'applicant_form.html'
    success_url = reverse_lazy('applicant-list')

class ApplicantUpdateView(UpdateView):
    model = Applicant
    fields = ['first_name', 'last_name', 'email', 'phone_number']
    template_name = 'applicant_form.html'
    success_url = reverse_lazy('applicant-list')

class ApplicantDeleteView(DeleteView):
    model = Applicant
    template_name = 'applicant_confirm_delete.html'
    success_url = reverse_lazy('applicant-list')


def home(request):
    return render(request, 'home.html')

def plot(request):
    # testing purposes
    #applicant_experiences = ApplicantExperience.objects.all()

    plot = request.GET.get('plot', '')

    if plot == 'dist-hab':
        plot_script, plot_div = distribucion_habilidades()
        title = "Distribución de Habilidades entre los Aplicantes"

    elif plot == 'exp-prom':
        plot_script, plot_div = experiencia_promedio_por_campo()
        title = "Experiencia Promedio por Campo"

    elif plot == 'cant-emp':
        plot_script, plot_div = cantidad_aplicantes_por_empresa()
        title = "Cantidad de Aplicantes por Empresa"
    
    elif plot == 'dist-cargo':
        plot_script, plot_div = distribucion_aplicantes_por_cargo()
        title = "Distribución de Aplicantes por Cargo"
    
    elif plot == 'hab-dem':
        plot_script, plot_div = habilidades_mas_demandadas_por_campo()
        title = "Habilidades Más Demandadas por Campo de Experiencia"
   
    elif plot == 'tend-exp':
        plot_script, plot_div = tendencias_aplicantes_por_ano_experiencia()
        title = "Tendencias de Aplicantes por Año de Experiencia"
    
    else:
        #return HttpResponse('Opción de gráfico no válida', status=400)
        plot_script, plot_div = distribucion_habilidades()
        title = "Distribución de Habilidades entre los Aplicantes"

    return render(request, 'plot.html',
                  {
                      #'applicant_experiences': applicant_experiences
                      'plot_script': plot_script,
                      'plot_div': plot_div,
                      'title': title
                      }
                  )