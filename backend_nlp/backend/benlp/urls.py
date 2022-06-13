from django.urls import path
# from .views import main
from .views import Summarizer_View
from . import views



urlpatterns = [
    # path('', main),
    # path('summarizer', SummarizerView.as_view()),
    # path('summarizer', SummarizerView.as_view()),
    path('summarizer', views.Summarizer_View, name='summarizer'),



]