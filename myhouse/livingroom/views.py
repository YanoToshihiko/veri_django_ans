from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class LivingRoomView(TemplateView):
    template_name = 'livingroom/home.html'


class WindowSideView(TemplateView):
    template_name = 'livingroom/window_side.html'
