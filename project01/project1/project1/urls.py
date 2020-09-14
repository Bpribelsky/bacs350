
from django.http import HttpResponse
from django.urls import path


def home_page_view(request):
    return HttpResponse("<h1>World Simplest Website</h1>")

def about_page_view(request):
    return HttpResponse("<h1>ABOUT</H1>")

urlpatterns = [
        path('', home_page_view),
        path('home', home_page_view),
        path('about', about_page_view),
        ]
