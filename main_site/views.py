from django.shortcuts import render
from django.views import generic


class HomePage(generic.TemplateView):
    """
    Displays the home page.
    """
    template_name = 'main/index.html'


class AboutPage(generic.TemplateView):
    template_name = 'main/about.html'


class ProductPage(generic.TemplateView):
    template_name = 'main/products.html'


class JobApplicationPage(generic.TemplateView):
    template_name = 'main/jobs.html'


class ContactPage(generic.TemplateView):
    template_name = 'main/contact.html'
