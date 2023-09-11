from django.shortcuts import render
from django.views import generic


class HomePage(generic.TemplateView):
    """
    Displays the home page.
    """
    template_name = 'main/index.html'
