from django.urls import path

from hero.views import HomeView, ThorView, HulkView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
     path('', HomeView.as_view()),
    path('thor', ThorView.as_view()),
    path('hulk', HulkView.as_view()),
]
