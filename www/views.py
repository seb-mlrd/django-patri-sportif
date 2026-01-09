from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import sportSite, site

# def home(request):
#     return HttpResponse("Welcome to the Home Page!")


class SportSiteList(ListView):
    model = sportSite
    template_name = 'site_list.html'
    context_object_name = 'sport_sites'
    paginate_by = 12
    ordering = ['appellation']

class SportSiteDetail(DetailView):
    model = sportSite
    template_name = 'site_detail.html'
    context_object_name = 'sport_site'
     