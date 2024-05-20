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

def dist_hab(request):
    # testing purposes
    #applicant_experiences = ApplicantExperience.objects.all()

    plot_script, plot_div = distribucion_habilidades()

    return render(request, 'dist_hab.html',
                  {
                      #'applicant_experiences': applicant_experiences
                      'plot_script': plot_script,
                      'plot_div': plot_div,
                      
                      }
                  )