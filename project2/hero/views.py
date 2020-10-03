from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse


class ThorView(TemplateView):
    template_name='Thor.html'

class HulkView(TemplateView):
    template_name='Hulk.html'
    
class HomeView(TemplateView):
    template_name='home.html'
