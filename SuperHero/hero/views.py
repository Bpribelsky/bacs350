from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import SuperHero

class PageView(TemplateView):
    def get_template_names(self):
        template_name = self.kwargs.get('template')
        return template_name

    
class IndexView(TemplateView):
    template_name = 'home.html'
    
    
class HeroView(ListView):
    def get_template_names(self):
        template_name = 'hero.html'
        return template_name
    
    def get_context_data(self, **kwargs):
        return{
            'hero': self.kwargs.get('hero')
        }
    model = SuperHero
    context_object_name = "all_heros_list"
        

class HomePageView(ListView):
    model = SuperHero
    template_name = 'home.html'
    context_object_name = "all_heros_list"

class DetailView(ListView):
    template_name = "detail.html"
    
    model = SuperHero
    context_object_name = "all_heros_list"
    
class addHeroView(CreateView):
    model = SuperHero
    template_name = "create.html"
    context_object_name = "all_heros_list"
    fields = '__all__'
    
class HeroEditView(CreateView):
    template_name = "hero_edit.html"
    model = SuperHero
    fields = '__all__'