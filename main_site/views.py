from django.shortcuts import render
from django.views import generic
from . import models


class HomePage(generic.TemplateView):
    """
    Displays the home page.
    """
    template_name = 'main/index.html'


class AboutPage(generic.TemplateView):
    """
    Displays the about page.
    """
    template_name = 'main/about.html'


class ProductPage(generic.ListView):
    """
    Display the products in the database on the products page, organized by
    category.
    """
    template_name = 'main/products.html'
    queryset = models.Product.objects.order_by('-date_added')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['types'] = models.PRODUCT_TYPE
        return context


class JobApplicationPage(generic.TemplateView):
    template_name = 'main/jobs.html'


class ContactPage(generic.TemplateView):
    template_name = 'main/contact.html'
