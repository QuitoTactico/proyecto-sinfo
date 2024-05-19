"""
URL configuration for sinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graficacion.views import (
    ApplicantListView,
    ApplicantDetailView,
    ApplicantCreateView,
    ApplicantUpdateView,
    ApplicantDeleteView
)

# forma como se deben realizar las busquedas:
# http://127.0.0.1:8000/applicants/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('applicants/', ApplicantListView.as_view(), name='applicant-list'),
    path('applicant/<int:pk>/', ApplicantDetailView.as_view(), name='applicant-detail'),
    path('applicant/new/', ApplicantCreateView.as_view(), name='applicant-create'),
    path('applicant/<int:pk>/edit/', ApplicantUpdateView.as_view(), name='applicant-update'),
    path('applicant/<int:pk>/delete/', ApplicantDeleteView.as_view(), name='applicant-delete'),
]
