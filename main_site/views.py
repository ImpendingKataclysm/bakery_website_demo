from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from . import models, forms


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


class JobApplicationPage(generic.FormView):
    """
    Display job application form on the Careers page. When the form is submitted,
    save the applicant to the database
    """
    form_class = forms.ApplicantForm
    template_name = 'main/jobs.html'
    success_url = '/'

    def form_valid(self, form):
        success_message = 'Thank you for your application!'
        applicant = form.save(commit=False)

        applicant.save()
        messages.success(self.request, message=success_message)

        return super().form_valid(form)


class ContactPage(generic.FormView):
    """
    Display the contact page with the contact form. When a message is received
    and successfully validated, it is stored in the Contact Messages table in
    the database and the user is redirected to the home page with a success
    message.
    """
    form_class = forms.ContactForm
    template_name = 'main/contact.html'
    success_url = '/'

    def form_valid(self, form):
        success_message = 'Thanks for reaching out!'
        form.save()
        messages.success(self.request, success_message)

        return super().form_valid(form)
