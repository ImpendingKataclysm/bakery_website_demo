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
    form_class = forms.ApplicantForm
    template_name = 'main/jobs.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        success_message = 'Thank you for your application!'
        applicant = form.save(commit=False)

        applicant.save()
        messages.success(self.request, message=success_message)

        return super().form_valid(form)


class ContactPage(generic.TemplateView):
    template_name = 'main/contact.html'
