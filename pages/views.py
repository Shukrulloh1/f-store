from django.shortcuts import render
from django.views.generic import TemplateView, CreateView


class HomePageView(TemplateView):
    template_name = 'main/index.html'


class ContactView(TemplateView):
    template_name = 'main/contact.html'




