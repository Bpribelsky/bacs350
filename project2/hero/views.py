from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse


class ThorView(TemplateView):
    template_name='thor.html'

class HulkView(TemplateView):
    template_name='hulk.html'
    
class HomeView(TemplateView):
    template_name='home.html'
