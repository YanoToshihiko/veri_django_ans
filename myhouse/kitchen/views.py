from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class KitchenView(TemplateView):
    template_name = 'kitchen/home.html' 