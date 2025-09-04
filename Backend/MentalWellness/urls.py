from django.contrib import admin
from django.urls import path, include
# from  get_motivational_quote,get_mentalwellness_quote

from . import views

urlpatterns = [
    path('quotesmo/',views.get_motivational_quote,name='motivational_quotes'),
    path('quotesme/',views.get_mentalwellness_quote,name='mentalwellness_quotes'),
]
